import pytest

from repositories_reader import RepositoriesReader

@pytest.fixture
def repositories_reader():
    return RepositoriesReader() 

def test_file_existence(repositories_reader):
    assert repositories_reader.open_repositories_file() is not None

def test_file_content(repositories_reader):
	assert repositories_reader.read_repositories_file() is not None