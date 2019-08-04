# -*- coding: utf-8 -*-

from scraper.repositories_reader import open_repositories_file, read_repositories_file

def test_file_existence():
	assert open_repositories_file() is not None

def test_file_content():
	assert read_repositories_file() is not None