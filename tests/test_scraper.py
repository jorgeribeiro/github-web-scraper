# -*- coding: utf-8 -*-

import pytest

from scraper import is_valid_repository, pull_folder_content, pull_file_content

def test_valid_repo_string():
	assert is_valid_repository('username/repository') is True

@pytest.mark.parametrize(
	'repo', (
		'not-a-user/not-a-repo/not-nothing',
		'/////////////',
		'user/repo/',
		'/')
	)
def test_invalid_repo_string(repo):
	assert is_valid_repository(repo) is False

def test_pull_valid_folder():
	assert pull_folder_content('jorgimello/github-web-scraper') is not None

def test_pull_invalid_folder():
	assert pull_folder_content('not-a-folder') is None

def test_pull_valid_file():
	assert pull_file_content('jorgimello/github-web-scraper/blob/master/repositories.txt') is not None

def test_pull_invalid_file():
	assert pull_file_content('jorgimello/github-web-scraper/tree/master/tests') is None
