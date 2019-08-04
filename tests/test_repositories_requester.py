# -*- coding: utf-8 -*-

from scraper.repositories_requester import request_url

TEST_REPO = 'jorgimello/github-web-scraper'

def test_url_request():
	assert request_url(TEST_REPO) is not None