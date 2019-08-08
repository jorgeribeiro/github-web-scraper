# -*- coding: utf-8 -*-

import pytest

from utils import is_valid_repository, calculate_bytes

def test_valid_repo_string():
    assert is_valid_repository('username/repository') is True

@pytest.mark.parametrize('repo', ('not-a-user/not-a-repo/not-nothing', '/////////////', 'user/repo/', '/'))
def test_invalid_repo_string(repo):
    assert is_valid_repository(repo) is False

@pytest.mark.parametrize('l', ('15 Bytes', '1.56 KB', '1.5 MB'))
def test_valid_list_calculate_bytes(l):
    assert calculate_bytes(l) >= 0

@pytest.mark.parametrize('l', ('15 Bytes x', '0 GB', 'random', 'number Bytes', '15 B'))
def test_calc_bytes_on_non_file(l):
    assert calculate_bytes(l) == -1