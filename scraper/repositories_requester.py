# -*- coding: utf-8 -*-

"""
Verificar necessidade desse script
"""

import requests

GITHUB_BASE_URL = 'https://github.com/'

def request_repo(repository):
	r = requests.get(GITHUB_BASE_URL + repository)
	return r