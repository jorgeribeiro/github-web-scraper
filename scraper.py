# -*- coding: utf-8 -*-

from repositories_reader import read_repositories_file
from repositories_requester import request_url
from utils import is_valid_repository, calculate_bytes

import re
from bs4 import BeautifulSoup

def pull_folder_content(url):
    # Extrai conteúdo de um diretório
    # Retorna html do tbody da tabela que contém os itens do diretório
    response = request_url(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.tbody

FILE_ELEMENT_FINDER = 'div'
FILE_CLASS_FINDER = 'text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0'
def pull_file_content(url):
    # Extrai conteúdo de um arquivo
    # Retorna html da div que contém informações do arquivo
    response = request_url(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find(FILE_ELEMENT_FINDER, class_=FILE_CLASS_FINDER)

def retrieve_lines_and_bytes_from_file(url):
    # Extrai número de linhas e bytes de um arquivo
    div = pull_file_content(url)
    div_text = [t.strip() for t in div.get_text().splitlines() if t.strip() != '']
    l, b = div_text[0], div_text[1]
    lines = [int(s) for s in l.split() if s.isdigit()][0]
    bytes_ = calculate_bytes(b)
    return lines, bytes_

PATH_TO_FOLDERS = '/tree/master'
PATH_TO_FILES = '/blob/master'
def separate_folders_and_files(folder_html):
    # TODO: incluir testes
    # Utiliza o método find_all do BealtifulSoup para diferenciar diretórios e arquivos
    # Retorna html onde são encontrados os padrões de referência para diretório e arquivo
    folders = folder_html.find_all(href=re.compile(PATH_TO_FOLDERS))
    files = folder_html.find_all(href=re.compile(PATH_TO_FILES))
    return folders, files

def extract_content_href(repository_html):
    # TODO: incluir testes
    # Extrai href de elementos que contenham links para diretórios e arquivos
    # Retorna lista com os hrefs encontrados
    folders_html, files_html = separate_folders_and_files(repository_html)
    hrefs_to_folders = [html['href'] for html in folders_html]
    hrefs_to_files = [html['href'] for html in files_html]
    return hrefs_to_folders, hrefs_to_files

def explore_repo(repository_html):
    # TODO: continuar método
    folders, files = extract_content_href(repository_html)
    for f in folders:
        print(f)
    for f in files:
        print(f)

# 1. Carregar lista de repositórios
repo_names = read_repositories_file()
# 2. Realizar exploração em cada repositório
# Operações: ler linhas, gerar árvore e salvar arquivo .txt
for repo_name in repo_names:
    if not is_valid_repository(repo_name): 
        continue
    project_root_html = pull_folder_content(repo_name)
    # Se html não vazio, repositório encontrado => realizar exploração
    if project_root_html: 
        explore_repo(project_root_html)
        
# Ideia de como armazenar extensões, linhas e bytes:
# Um dict pra armazenar número de linhas e bytes, e uma lista pra guardar as keys
# files = {'js': {'lines': 9, 'bytes': 15}, 'txt': {'lines': 10, 'bytes': 15}, 'yml': {'lines': 20, 'bytes': 30}}
# extensions = ['js', 'txt', 'yml']