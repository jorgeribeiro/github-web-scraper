# -*- coding: utf-8 -*-

from scraper import repositories_requester

TEST_REPO = 'jorgimello/github-web-scraper'

def test_request_repo():
	assert repositories_requester.request_repo(TEST_REPO) is not None