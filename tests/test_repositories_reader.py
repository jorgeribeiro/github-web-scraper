# -*- coding: utf-8 -*-

from scraper import repositories_reader

def test_open_repositories_file():
	assert repositories_reader.open_repositories_file() is not None

def test_read_repositories_file():
	assert repositories_reader.read_repositories_file() is not None