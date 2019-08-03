from scraper import RepositoriesReader

class TestRepositoriesReader(RepositoriesReader):
    def test_file_existence(self):
        self.repositories_reader = RepositoriesReader()
        assert self.repositories_reader.open_repositories_file() is not None