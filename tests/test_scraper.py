# -*- coding: utf-8 -*-

import pytest

from scraper import pull_folder_content, pull_file_content, retrieve_lines_and_bytes_from_file, separate_folders_and_files, extract_content_href

def test_pull_valid_folder():
    assert pull_folder_content('jorgimello/github-web-scraper') is not None

def test_pull_invalid_folder():
    assert pull_folder_content('not-a-folder') is None

def test_pull_valid_file():
    assert pull_file_content('jorgimello/github-web-scraper/blob/master/repositories.txt') is not None

def test_pull_invalid_file():
    assert pull_file_content('jorgimello/github-web-scraper/tree/master/tests') is None