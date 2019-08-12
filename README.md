# Github Web Scraper

[![Build Status](https://travis-ci.com/jorgimello/github-web-scraper.svg?branch=master)](https://travis-ci.com/jorgimello/github-web-scraper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/16f28c79be014c7bb40557ecaf4de161)](https://www.codacy.com/app/jorgimello/github-web-scraper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jorgimello/github-web-scraper&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/16f28c79be014c7bb40557ecaf4de161)](https://www.codacy.com/app/jorgimello/github-web-scraper?utm_source=github.com&utm_medium=referral&utm_content=jorgimello/github-web-scraper&utm_campaign=Badge_Coverage)

Web scraping que busca informações de projetos públicos do Github e compila os dados obtidos em arquivos .txt. Esses arquivos incluem informações como quantidade de linhas (total e percentual) de cada extensão de arquivo e a estrutura de pastas do projeto.

## Versão do Python
3.5.2

## Dependências
- Beautiful Soup
- requests
- pytest

## Instalação
[Em construção]

## Ideias
- Utilizei a biblioteca multiprocessing para fazer a exploração dos repositórios com Bealtiful Soup de forma assíncrona
- Não faz uso de bibliotecas para construir e imprimir a árvore de arquivos. Tudo é tratado pelo método recursivo explore_repository em scraper.py
- Realiza a contagem de bytes de arquivos que não possuam linhas de código

## Melhorias
Aplicar uma estrutura de árvores com pais e filhos, estruturando o caminho das pastas e arquivos do repositório, e assim poder fazer a exploração das pastas de forma assíncrona.