# -*- coding: utf-8 -*-

from repositories_reader import read_repositories_file
from repositories_requester import request_url
from utils import is_valid_repository, get_folder_or_file_name, get_lines_and_bytes, generate_str_with_spaces, get_file_extension, print_to_file

import re
from bs4 import BeautifulSoup
from multiprocessing import Pool

def pull_folder_content(url):
    """
    Extrai conteúdo de um diretório
    Retorna soup.tbody da tabela que contém os itens do diretório
    """
    response = request_url(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.tbody

FILE_ELEMENT_FINDER = 'div'
FILE_CLASS_FINDER = 'text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0'
def pull_file_content(url):
    """
    Extrai conteúdo de um arquivo
    Retorna lista com informações do arquivo (linhas e bytes)
    """
    response = request_url(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find(FILE_ELEMENT_FINDER, class_=FILE_CLASS_FINDER)
    if div:
        return [t.strip() for t in div.get_text().splitlines() if t.strip() != '']
    else:
        return []

def include_extension_in_files_dict(f_dict, lines, bytes_, extension):
    """
    Adiciona extensão com linhas e bytes em um dict
    Formato do dict: {'extensão': {'lines', 'bytes'}}
    TODO: adicionar testes
    """
    if extension not in f_dict:
        f_dict[extension] = {'lines': lines, 'bytes': bytes_}
    else:
        current_lines, current_bytes = f_dict[extension]['lines'], f_dict[extension]['bytes']
        f_dict[extension] = {'lines': current_lines + lines, 'bytes': current_bytes + bytes_}
    return f_dict

REGEX_TO_FOLDERS = '/tree/master'
REGEX_TO_FILES = '/blob/master'
def extract_hrefs(repository_content):
    """
    Extrai href de elementos que contenham links para diretórios e arquivos
    Retorna lista com os hrefs encontrados
    """
    folders_html = repository_content.find_all(href=re.compile(REGEX_TO_FOLDERS))
    files_html = repository_content.find_all(href=re.compile(REGEX_TO_FILES))
    hrefs_to_folders = [html['href'] for html in folders_html]
    hrefs_to_files = [html['href'] for html in files_html]
    return hrefs_to_folders, hrefs_to_files

def explore_file(file):
    """
    Extrai conteúdo de arquivo
    Retorna nome, linhas, bytes e extensão do arquivo recebido
    """
    file_content = pull_file_content(file)
    lines, bytes_ = get_lines_and_bytes(file_content)
    filename = get_folder_or_file_name(file)
    if len(file_content) == 2:
        return filename, lines, bytes_, get_file_extension(filename)
    else:
        return filename, lines, bytes_, '<nloc>'    

def explore_repository(repo_name, depth=0, tree_str='', files_dict={}):
    """
    Método principal da aplicação
    Percorre recursivamente o repositório
    """
    repository_content = pull_folder_content(repo_name)
    if (repository_content):
        folders, files = extract_hrefs(repository_content)
        for f in folders:
            tree_str += generate_str_with_spaces(depth, get_folder_or_file_name(f), is_folder=True)
            tree_str, files_dict = explore_repository(f, depth + 1, tree_str)
        for f in files:
            filename, lines, bytes_, extension = explore_file(f)
            files_dict = include_extension_in_files_dict(files_dict, lines=lines, bytes_=bytes_, extension=extension)
            tree_str += generate_str_with_spaces(depth, filename, is_folder=False, loc=lines)            
        if depth == 0:
            print_to_file(repo_name, tree_str, files_dict)
        return tree_str, files_dict
    else:
        return

if __name__ == '__main__':
    repo_names = read_repositories_file()
    valid_repos = [repo for repo in repo_names if is_valid_repository(repo)]
    if len(valid_repos) >= 2:
        with Pool(3) as p:
            # Explorar até 3 repositórios paralelamente
            p.map(explore_repository, valid_repos)
    else:
        for valid_repo in valid_repos:
            explore_repository(valid_repo)

"""
Ideia de como armazenar extensões, linhas e bytes:
files = {'js': {'lines': 9, 'bytes': 15}, 'txt': {'lines': 10, 'bytes': 15}, 'yml': {'lines': 20, 'bytes': 30}}
files.keys() retorna extensões
usar <'extensao' in files> para verificar se extensão já existe. Ex: 'js' in files; 'py' in files
"""