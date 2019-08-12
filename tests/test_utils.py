# -*- coding: utf-8 -*-

import pytest

from utils import is_valid_repository, calculate_bytes, get_folder_or_file_name, get_lines_and_bytes, get_file_extension

def test_valid_repo_string():
    assert is_valid_repository('username/repository') is True

@pytest.mark.parametrize('repo', ('not-a-user/not-a-repo/not-nothing', '/////////////', 'user/repo/', '/'))
def test_invalid_repo_string(repo):
    assert is_valid_repository(repo) is False

@pytest.mark.parametrize('l', ('15 Bytes', '1.56 KB', '1.5 MB'))
def test_calculate_bytes_valid_args(l):
    assert calculate_bytes(l) >= 0

@pytest.mark.parametrize('l', ('15 Bytes x', '0 GB', 'text', 'number Bytes', '15 B'))
def test_calculate_bytes_invalid_args(l):
    assert calculate_bytes(l) == -1

def test_get_name_on_valid_href():
    assert get_folder_or_file_name('path/to/folder/or/file') != ''

def test_get_name_on_invalid_href():
    assert get_folder_or_file_name('pathtofolder') == ''

def test_get_name_with_no_args():
    assert get_folder_or_file_name() == ''

def test_get_lines_and_bytes_on_empty_list():
	assert get_lines_and_bytes(l = []) == -1

@pytest.mark.parametrize('l', (['36 lines (25 sloc)', '1.29 KB'], ['11.9 KB'], ['executable file', '15 lines (15 sloc)', '1.75 KB']))
def test_get_lines_and_bytes_on_valid_args(l):
	assert get_lines_and_bytes(l) != -1

def test_get_lines_and_bytes_on_no_lines_file():
	lines, bytes_ = get_lines_and_bytes(['11.9 KB'])
	assert lines == 0
	assert bytes_ == 11.9 * 1024

def test_get_file_extensions():
    assert get_file_extension('.gitignore') == '<outros>'
    assert get_file_extension('Makefile') == '<outros>'
    assert get_file_extension('file.txt') == 'txt'
    assert get_file_extension('file.txt~') == 'txt'
    assert get_file_extension('.file.yml') == 'yml'