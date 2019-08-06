# -*- coding: utf-8 -*-

import requests

GITHUB_BASE_URL = 'https://github.com'

def request_url(url = ''):
	r = requests.get(GITHUB_BASE_URL + '/' + url)
	return r