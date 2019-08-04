# -*- coding: utf-8 -*-

from scraper.repositories_requester import request_repo

TEST_REPO = 'jorgimello/github-web-scraper'

def test_repo_request():
	assert request_repo(TEST_REPO) is not None