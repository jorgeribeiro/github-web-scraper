# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from scraper import pull_folder_content, pull_file_content, extract_hrefs, explore_file, include_extension_in_files_dict

def test_pull_on_valid_folder():
    assert pull_folder_content('jorgimello/github-web-scraper')

def test_pull_on_invalid_folder():
    assert pull_folder_content('invalid-user/invalid-folder') is None

def test_pull_on_valid_file():
    c = pull_file_content('jorgimello/github-web-scraper/blob/master/repositories.txt')
    assert len(c) > 0

def test_pull_on_invalid_file():
    c = pull_file_content('jorgimello/github-web-scraper/tree/master/tests')
    assert len(c) == 0

def test_extract_content_on_valid_folder():
	f = pull_folder_content('jorgimello/github-web-scraper')
	assert extract_hrefs(f)

def test_extract_content_on_empty_soup():
	soup = BeautifulSoup('', 'html.parser')
	assert extract_hrefs(soup)

def test_file_explore_on_regular_file():
    filename, lines, bytes_, extension = explore_file('jorgimello/github-web-scraper/blob/master/repositories.txt')
    assert filename == 'repositories.txt'
    assert lines >= 0
    assert bytes_ >= 0
    assert extension == 'txt'

def test_file_explore_on_non_lines_file():
    filename, lines, bytes_, extension = explore_file('vivadecora/backend-teste/blob/master/vivadecora-logo.png')
    assert filename == 'vivadecora-logo.png'
    assert lines == 0
    assert bytes_ >= 0
    assert extension == '<nloc>' # No lines of code

def test_include_file_in_dict():
    f_dict = {}
    f_dict = include_extension_in_files_dict(f_dict, 5, 10, 'js')
    assert 'js' in f_dict
    assert f_dict['js']['lines'] == 5
    assert f_dict['js']['bytes'] == 10

def test_include_file_with_extension_already_in_dict():
    f_dict = {'js': {'lines': 10, 'bytes': 15}, 'txt': {'lines': 10, 'bytes': 15}}
    f_dict = include_extension_in_files_dict(f_dict, 5, 10, 'js')
    assert f_dict['js']['lines'] == 10 + 5
    assert f_dict['js']['bytes'] == 15 + 10