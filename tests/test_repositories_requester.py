# -*- coding: utf-8 -*-

from repositories_requester import request_url

def test_existent_repo_url():
	assert request_url('jorgimello/github-web-scraper').status_code == 200

def test_non_existent_repo_url():
	assert request_url('not-a-user/not-a-repo').status_code == 404

def test_with_no_args():
	assert request_url()