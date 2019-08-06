# -*- coding: utf-8 -*-

from scraper import is_valid_repository

VALID_REPO = 'jorgimello/github-web-scraper'
def test_valid_repo_string():
	assert is_valid_repository(VALID_REPO) is True

INVALID_REPO = '////'
def test_invalid_repo_string():
	assert is_valid_repository(INVALID_REPO) is False