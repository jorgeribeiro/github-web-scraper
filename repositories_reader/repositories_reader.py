class RepositoriesReader:
    def open_repositories_file(self):
        try:
            f = open('../repositories.txt', 'r')
        except FileNotFoundError:
            print('repositories.txt not found. Creating...')
            f = open('../repositories.txt', 'w+')         
        return f

    def read_repositories_file(self):
        f = self.open_repositories_file()
        repos = [line.rstrip('\n').strip() for line in f]
        repos = filter(None, repos) # Remove strings vazias
        return repos
