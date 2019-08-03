# -*- coding: utf-8 -*-

import pytest
import repositories_reader

def test_file_existence():
    assert repositories_reader.open_repositories_file() is not None

def test_file_content():
	assert repositories_reader.read_repositories_file() is not None