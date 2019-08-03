# -*- coding: utf-8 -*-

"""
Verificar necessidade desse script
"""

import requests

def request_repo(repository):
	r = requests.get('https://github.com/' + repository)
	return r