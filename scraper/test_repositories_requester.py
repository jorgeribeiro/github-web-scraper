# -*- coding: utf-8 -*-

import pytest
import repositories_requester

def test_request():
	assert repositories_requester.request_repo('jorgimello/github-web-scraper').status_code == 200