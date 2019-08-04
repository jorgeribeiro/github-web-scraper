# -*- coding: utf-8 -*-

import requests

GITHUB_BASE_URL = 'https://github.com'

def request_repo(repository_path):
	r = requests.get(GITHUB_BASE_URL + '/' + repository_path)
	return r

def request_href(href):
	r = requests.get(GITHUB_BASE_URL + href)
	return r