# -*- coding: utf-8 -*-

def open_repositories_file():
    try:
        f = open('../repositories.txt', 'r')
    except FileNotFoundError:
        print('repositories.txt not found. Creating...')
        f = open('../repositories.txt', 'w+')         
    return f

def read_repositories_file():
    f = open_repositories_file()
    repos = [line.rstrip('\n').strip() for line in f]
    return repos
