# -*- coding: utf-8 -*-

from repositories_requester import request_url

VALID_REPO = 'jorgimello/github-web-scraper'
def test_valid_repo_url():
	assert request_url(url = VALID_REPO).status_code == 200

INVALID_REPO = 'not-a-user/not-a-repo'
def test_invalid_repo_url():
	assert request_url(url = INVALID_REPO).status_code == 404

def test_with_no_args():
	assert request_url()

def test_random_url():
	assert request_url(url = 'random')