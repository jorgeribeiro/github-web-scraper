# -*- coding: utf-8 -*-

from repositories_reader import read_repositories_file
from repositories_requester import request_url
from utils import is_valid_repository, calculate_bytes, get_folder_or_file_name, generate_str_with_spaces

import re
from bs4 import BeautifulSoup
from multiprocessing import Pool

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
    """
    div = pull_file_content(url)
    if div:
        div_text = [t.strip() for t in div.get_text().splitlines() if t.strip() != '']
        if len(div_text) == 2:
            lines = [int(s) for s in div_text[0].split() if s.isdigit()][0]
            bytes_ = calculate_bytes(div_text[1])
            return lines, bytes_            
        else:
            # Se o arquivo não possuir linhas (se for uma imagem, por exemplo)
            lines = 0
            bytes_ = calculate_bytes(div_text[0])
            return lines, bytes_
    else:
        return -1

REGEX_TO_FOLDERS = '/tree/master'
REGEX_TO_FILES = '/blob/master'
def extract_hrefs(repository_content):
    """Extrai href de elementos que contenham links para diretórios e arquivos
    Retorna lista com os hrefs encontrados
    """
    folders_html = repository_content.find_all(href=re.compile(REGEX_TO_FOLDERS))
    files_html = repository_content.find_all(href=re.compile(REGEX_TO_FILES))
    hrefs_to_folders = [html['href'] for html in folders_html]
    hrefs_to_files = [html['href'] for html in files_html]
    return hrefs_to_folders, hrefs_to_files

def explore_repository(repository_content, depth):
    """Método principal da aplicação
    Percorre recursivamente o repositório
    TODO: armazenar tudo no .txt
    TODO: utilizar dict global para armazenar linhas e bytes dos arquivos
    """
    folders, files = extract_hrefs(repository_content)
    for f in folders:
        print(generate_str_with_spaces(depth, get_folder_or_file_name(f), is_folder=True))
        ff = pull_folder_content(f)
        if ff:
            explore_repository(ff, depth + 1)
    with Pool(10) as p:
        records = p.map(retrieve_lines_and_bytes_from_file, files)
    for f in files:
        print(generate_str_with_spaces(depth, get_folder_or_file_name(f), is_folder=False))
    return

repo_names = read_repositories_file()
for repo_name in repo_names:
    if not is_valid_repository(repo_name):
        continue
    repo_root = pull_folder_content(repo_name)
    if repo_root:
        explore_repository(repo_root, depth=0)

"""
Ideia de como armazenar extensões, linhas e bytes:
files = {'js': {'lines': 9, 'bytes': 15}, 'txt': {'lines': 10, 'bytes': 15}, 'yml': {'lines': 20, 'bytes': 30}}
files.keys() retorna extensões
usar <'extensao' in files> para verificar se extensão já existe. Ex: 'js' in files; 'py' in files
"""