import repositories_reader
import repositories_requester

from bs4 import BeautifulSoup

def scraper():
	repos = repositories_reader.read_repositories_file()
	print(repos)

scraper()	