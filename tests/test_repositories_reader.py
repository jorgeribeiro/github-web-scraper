# -*- coding: utf-8 -*-

from repositories_reader import open_repositories_file, read_repositories_file

def test_file_existence():
	assert open_repositories_file()

def test_repo_list_is_created():
	assert len(read_repositories_file()) >= 0