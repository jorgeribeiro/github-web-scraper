# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from scraper import pull_folder_content, pull_file_content, retrieve_lines_and_bytes_from_file, extract_hrefs

def test_pull_on_valid_folder():
    assert pull_folder_content('jorgimello/github-web-scraper')

def test_pull_on_invalid_folder():
    assert pull_folder_content('not-a-folder') is None

def test_pull_on_valid_file():
    assert pull_file_content('jorgimello/github-web-scraper/blob/master/repositories.txt')

def test_pull_on_invalid_file():
    assert pull_file_content('jorgimello/github-web-scraper/tree/master/tests') is None

def test_retrieve_lines_and_bytes_on_file():
	assert retrieve_lines_and_bytes_from_file('jorgimello/github-web-scraper/blob/master/repositories.txt') != -1

def test_retrieve_lines_and_bytes_on_non_lines_file():
	lines, bytes_ = retrieve_lines_and_bytes_from_file('vivadecora/backend-teste/blob/master/vivadecora-logo.png')	
	assert lines == 0
	assert bytes_ >= 0

def test_retrieve_lines_and_bytes_on_non_file():
	assert retrieve_lines_and_bytes_from_file('jorgimello') == -1

def test_extract_content_on_valid_folder():
	f = pull_folder_content('jorgimello/github-web-scraper')
	assert extract_hrefs(f)

def test_extract_content_on_empty_soup():
	soup = BeautifulSoup('', 'html.parser')
	assert extract_hrefs(soup)