from repositories_reader import RepositoriesReader

r = RepositoriesReader() 
l = r.read_repositories_file()
print(len(l))