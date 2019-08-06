# -*- coding: utf-8 -*-

import pytest

from scraper import is_valid_repository

def test_valid_repo_string():
	assert is_valid_repository('username/repository') is True

@pytest.mark.parametrize('repo', ('not-a-user/not-a-repo/not-nothing', '/////////////', 'user/repo/'))
def test_invalid_repo_string(repo):
	assert is_valid_repository(repo) is False