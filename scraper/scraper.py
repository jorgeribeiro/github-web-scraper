class RepositoriesReader:
    def open_repositories_file(self):
        try:
            self.f = open('repositories.txt', 'r')
        except FileNotFoundError:
            print('repositories.txt not found. Creating...')
            self.f = open('repositories.txt', 'w+')
        return self.f

    def read_repositories(self):
        