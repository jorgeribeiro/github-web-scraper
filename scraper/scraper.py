# -*- coding: utf-8 -*-

from repositories_reader import read_repositories_file
from repositories_requester import request_repo

import requests
import re
from bs4 import BeautifulSoup

# 1. Carregar lista de repositórios
repos = read_repositories_file()

# TODO #1: validar repositório pelo formato da string: [texto;hífen;ponto]/[texto;hífen;ponto]

# 2. Realizar operações em cada repositório
	# Operações: ler linhas, gerar árvore e salvar arquivo .txt
for r in repos:
	response = request_repo(r)
	soup = BeautifulSoup(response.text, 'html.parser')

	project_root_links = soup.tbody
	if (project_root_links): # Possível consertar com TODO #1
		folders = project_root_links.find_all(href=re.compile(r + '/tree/master'))
		files = project_root_links.find_all(href=re.compile(r + '/blob/master'))
		
		for i in folders:
			print(i['href'])

		for j in files:
			print(j['href'])