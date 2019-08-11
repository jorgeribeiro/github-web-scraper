# -*- coding: utf-8 -*-

import re
import os

def is_valid_repository(repository_string):
    """
    Verifica se repositório está no formato <dono-do-projeto>/<nome-do-projeto>
    Evita requests em links existentes, mas que não estão no formato válido
    """
    words = repository_string.split('/')
    if len(repository_string) >= 3 and len(words) == 2:
        return True
    return False

def calculate_bytes(size_unit_str):
    """
    Calcula bytes de um arquivo
    Recebe uma string de tamanho 2 no formato 'size unit'
    """
    try:
        size, unit = size_unit_str.split()
        if unit == 'Bytes':
            return float(size)
        elif unit == 'KB':
            return float(size) * 1024.0
        elif unit == 'MB':
            return float(size) * 1024.0 * 1024.0
        else:
            return -1
    except ValueError:
        return -1

def get_folder_or_file_name(href=''):
    """
    Retorna nome do diretório ou arquivo
    Recebe uma string no formato caminho/para/diretorio
    ou caminho/para/arquivo
    """
    name = href.split('/')
    if len(name) > 1:
        return name[-1]
    else:
        return ''

def get_lines_and_bytes(l):
    """
    Retorna quantidade de linhas e bytes
    Recebe uma lista de tamanho dois (para arquivos com linhas de código)
    ou tamanho um (para arquivos sem linhas de código)
    """
    if len(l) == 2:
        lines = [int(s) for s in l[0].split() if s.isdigit()][0]
        bytes_ = calculate_bytes(l[1])
        return lines, bytes_           
    elif len(l) == 1:
        # Se o arquivo não possuir linhas (se for uma imagem, por exemplo)
        lines = 0
        bytes_ = calculate_bytes(l[0])
        return lines, bytes_
    else:
        return -1

def generate_str_with_spaces(depth, folder_or_file_name, is_folder, loc=0):
    """
    Gera string com espaços de acordo com depth
    String gerada é utilizada para imprimir árvore de arquivos
    """
    s = ''
    for _ in range(depth):
        s += '|'
        for _ in range(3):
            s += ' '
    if is_folder:
        return s + '|__[' + folder_or_file_name + ']\n'
    else:
        return s + '|__' + folder_or_file_name + ' (' + str(loc) + ' linhas)\n'

def get_file_extension(filename):
    """
    Retorna tipo de extensão a partir do nome do arquivo
    Verifica também casos em que não há extensão definida
    """
    s = filename.split('.')
    if len(s) == 1:
        # Arquivos sem extensão. Ex: Dockerfile
        return '<outros>'
    elif len(s) == 2 and s[0] == '':
        # Arquivos sem extensão mas que apresentem ponto. Ex: .htaccess
        return '<outros>'
    else:
        # Arquivos com extensão. Retorna a extensão removendo caracteres especiais
        return re.sub('[!@#$~,;´`]', '', s[-1])

def generate_extensions_table(files_dict):
    s = ''
    total_lines = sum(f['lines'] for f in files_dict.values())
    total_bytes = sum(f['bytes'] for f in files_dict.values())
    print(total_lines, total_bytes)
    # s += '    Extensão    |    Linhas    |    Bytes    \n'
    

EXPLORED_REPOS_FOLDER = 'explored_repos/'
def print_to_file(repo_name, tree_str, files_dict):
    """
    Escreve arquivo com informações do repositório explorado
    Verifica existência do diretório EXPLORED_REPOS_FOLDER, que é criado caso não exista
    """
    if not os.path.isdir(os.getcwd() + '/' + EXPLORED_REPOS_FOLDER):
        os.mkdir(EXPLORED_REPOS_FOLDER)
    filename = repo_name.replace('/', '_') + '.txt'
    with open(os.getcwd() + '/' + EXPLORED_REPOS_FOLDER + filename, 'w+') as file:
        file.write('[Repositório ' + repo_name + ']\n')
        file.write(tree_str)