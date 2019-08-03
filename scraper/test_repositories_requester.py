# -*- coding: utf-8 -*-

"""
Verificar necessidade desse teste
"""

import pytest
import repositories_requester

def test_request():
	assert repositories_requester.request_repo('jorgimello/github-web-scraper') is not None