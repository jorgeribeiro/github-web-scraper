# -*- coding: utf-8 -*-

import re
import math
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
        return name[-1].replace('%20', ' ') # %20 equivale a um espaço no href        
    else:
        return ''

def get_lines_and_bytes(l):
    """
    Retorna quantidade de linhas e bytes de um arquivo
    Recebe como argumento uma lista com os dados do arquivo
    """
    if len(l) == 3: # ['text', 'n lines', 'm Bytes']
        lines = [int(s) for s in l[1].split() if s.isdigit()][0]
        bytes_ = calculate_bytes(l[2])
        return lines, bytes_
    elif len(l) == 2: # ['n lines', 'm Bytes'] ou ['text', 'm Bytes']
        digit_found = [int(s) for s in l[0].split() if s.isdigit()]
        if digit_found:
            lines = [int(s) for s in l[0].split() if s.isdigit()][0]
        else:
            lines = 0
        bytes_ = calculate_bytes(l[1])
        return lines, bytes_
    elif len(l) == 1: # ['m Bytes']
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
        return s[-1]

def add_spaces(limit, s):
    """
    Gera espaços em branco para formatar tabela de extensões
    a partir do limite informado como argumento
    """
    length = limit - len(s)
    s = ''
    for _ in range(length):
        s += ' '
    return s + '|'

def generate_extensions_table(files_dict):
    """
    Recebe dict na forma {'extensão': {'lines', 'bytes'}}
    e retorna a string de uma tabela com extensões, linhas e bytes
    """
    s = ''
    total_lines = sum(f['lines'] for f in files_dict.values())
    total_bytes = sum(f['bytes'] for f in files_dict.values())
    s += '|       Extensão       |        Linhas        |        Bytes         |\n'
    for k in files_dict.keys():
        l = str(files_dict[k]['lines']) + ' (' + '%.1f' % (files_dict[k]['lines'] / total_lines * 100) + '%)' if total_lines != 0 else 0
        b = str('%.1f' % (files_dict[k]['bytes'])) + ' (' + '%.1f' % (files_dict[k]['bytes'] / total_bytes * 100) + '%)' if total_bytes != 0 else 0
        ext = k + add_spaces(22, k)        
        lines = l + add_spaces(22, l)
        bytes_ = b + add_spaces(22, b)
        s += '|' + ext + lines + bytes_ + '\n'
    return s

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
        file.write(tree_str + '\n')
        file.write(generate_extensions_table(files_dict))
