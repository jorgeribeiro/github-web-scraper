# -*- coding: utf-8 -*-

REPOSITORIES_FILENAME = 'repositories.txt'

def open_repositories_file():
    try:
        f = open(REPOSITORIES_FILENAME, 'r')
    except FileNotFoundError:
        f = open(REPOSITORIES_FILENAME, 'w+')
    return f

def read_repositories_file():
    f = open_repositories_file()
    repos = [line.rstrip('\n').strip() for line in f]
    return repos
