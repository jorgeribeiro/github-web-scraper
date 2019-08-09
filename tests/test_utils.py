# -*- coding: utf-8 -*-

import pytest

from utils import is_valid_repository, calculate_bytes, get_folder_or_file_name

def test_valid_repo_string():
    assert is_valid_repository('username/repository') is True

@pytest.mark.parametrize('repo', ('not-a-user/not-a-repo/not-nothing', '/////////////', 'user/repo/', '/'))
def test_invalid_repo_string(repo):
    assert is_valid_repository(repo) is False

@pytest.mark.parametrize('l', ('15 Bytes', '1.56 KB', '1.5 MB'))
def test_calculate_bytes_valid_args(l):
    assert calculate_bytes(l) >= 0

@pytest.mark.parametrize('l', ('15 Bytes x', '0 GB', 'random', 'number Bytes', '15 B'))
def test_calculate_bytes_invalid_args(l):
    assert calculate_bytes(l) == -1

def test_get_name_on_valid_href():
    assert get_folder_or_file_name('path/to/folder/or/file') != ''

def test_get_name_on_invalid_href():
    assert get_folder_or_file_name('pathtofolder') == ''

def test_get_name_on_empty_href():
    assert get_folder_or_file_name('') == ''

def test_get_name_with_no_args():
    assert get_folder_or_file_name() == ''