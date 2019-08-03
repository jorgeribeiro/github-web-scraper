# -*- coding: utf-8 -*-

from repositories_reader import read_repositories_file
from repositories_requester import request_repo

import requests
from bs4 import BeautifulSoup

def scrap_table():
	repos = read_repositories_file()
	response = request_repo(repos[0])

	soup = BeautifulSoup(response.text, 'html.parser')
	a = soup.findAll('a', {'class': 'js-navigation-open'})
	for i in a:
		if len(i['href']) > 0:
			print(i['href'])

# 1. Carregar lista de repositórios
repos = read_repositories_file()

# 2. Realizar operações em cada repositório
for r in repos:
	response = request_repo(r)
	soup = BeautifulSoup(response.text, 'html.parser')