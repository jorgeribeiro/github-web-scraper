# -*- coding: utf-8 -*-

from repositories_reader import read_repositories_file
from repositories_requester import request_url
from utils import is_valid_repository, calculate_bytes, get_folder_or_file_name

import re
from bs4 import BeautifulSoup

def pull_folder_content(url):
    """Extrai conteúdo de um diretório
    Retorna soup.tbody da tabela que contém os itens do diretório
    """
    response = request_url(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.tbody

FILE_ELEMENT_FINDER = 'div'
FILE_CLASS_FINDER = 'text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0'
def pull_file_content(url):
    """Extrai conteúdo de um arquivo
    Retorna soup.div que contém informações do arquivo
    """
    response = request_url(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find(FILE_ELEMENT_FINDER, class_=FILE_CLASS_FINDER)

def retrieve_lines_and_bytes_from_file(url):
    """Extrai número de linhas e bytes de um arquivo
    Retorna linhas e bytes se a div for encontrada
    TODO: possível refatoramento => receber apenas texto em vez do link do arquivo
    TODO: verificar casos de arquivos sem linhas. Ex: https://github.com/vivadecora/backend-teste/blob/master/vivadecora-logo.png
    """
    div = pull_file_content(url)
    if div:
        div_text = [t.strip() for t in div.get_text().splitlines() if t.strip() != '']
        l, b = div_text[0], div_text[1]
        lines = [int(s) for s in l.split() if s.isdigit()][0]
        bytes_ = calculate_bytes(b)
        return lines, bytes_
    else:
        return -1

PATH_TO_FOLDERS = '/tree/master'
PATH_TO_FILES = '/blob/master'
def extract_hrefs(repository_content):
    """Extrai href de elementos que contenham links para diretórios e arquivos
    Retorna lista com os hrefs encontrados
    """
    folders_html = repository_content.find_all(href=re.compile(PATH_TO_FOLDERS))
    files_html = repository_content.find_all(href=re.compile(PATH_TO_FILES))
    hrefs_to_folders = [html['href'] for html in folders_html]
    hrefs_to_files = [html['href'] for html in files_html]
    return hrefs_to_folders, hrefs_to_files

def explore_repo_recursively(repository_content):
    """Método principal da aplicação
    Percorre recursivamente o repositório
    TODO: imprimir conteúdo do repositório em forma de árvore
    TODO: fazer requests nos arquivos e calcular linhas e bytes
    TODO: armazenar tudo no .txt
    """
    folders, files = extract_hrefs(repository_content)
    for f in folders:
        print(get_folder_or_file_name(f))
        ff = pull_folder_content(f)
        if ff:
            explore_repo_recursively(ff)
    for f in files:
        print(get_folder_or_file_name(f))
    return

repo_names = read_repositories_file()
# 1. Carregar lista de repositórios
for repo_name in repo_names:
    # 2. Realizar exploração em cada repositório
    if not is_valid_repository(repo_name):
        continue
    repo_root = pull_folder_content(repo_name)
    if repo_root:
        # Se repo_root não nulo, repositório encontrado => realizar exploração
        explore_repo_recursively(repo_root)

"""
Ideia de como armazenar extensões, linhas e bytes:
files = {'js': {'lines': 9, 'bytes': 15}, 'txt': {'lines': 10, 'bytes': 15}, 'yml': {'lines': 20, 'bytes': 30}}
files.keys() retorna extensões
usar <'extensao' in files> para verificar se extensão já existe. Ex: 'js' in files; 'py' in files
"""