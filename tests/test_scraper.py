# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from scraper import pull_folder_content, pull_file_content, extract_hrefs

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