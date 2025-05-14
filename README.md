# Github Web Scraper

Web scraping que busca informações de projetos públicos do Github e compila os dados obtidos em arquivos .txt. Esses arquivos incluem informações como quantidade de linhas (total e percentual) de cada extensão de arquivo e a estrutura de pastas do projeto.

## Versão do Python
3.5.2

## Dependências
- Beautiful Soup
- requests
- pytest

## Instalação
1. `git clone https://github.com/jorgimello/github-web-scraper.git`
2. `cd github-web-scraper/`
3. `pipenv install` (cria um virtualenv com as dependências)
4. `pipenv shell` (para ativar o virtualenv. Etapa é necessária sempre que abrir um terminal novo dentro da pasta do projeto)

## Como utilizar
Após executar os passos acima corretamente, execute `python scraper.py` dentro da pasta do projeto. Caso o arquivo `repositories.txt` não exista, o programa criará um na raiz do projeto. Adicione os repositórios que deseja realizar o scraping nesse .txt (cada um em uma linha diferente) no formato `username/repositorio` (exemplo: `jorgimello/heart-disease-classifier`) e execute `python scraper.py` novamente.

Para executar os testes unitários, basta executar `pytest` dentro da pasta do projeto.

Ao iniciar o scraping em um repositório, no console será mostrada a mensagem `[+] Scraping no repositório user/repositorio iniciado...` e ao finalizar, `[+] Scraping no repositório user/repositorio iniciado finalizado!`. Para repositórios muito grandes, o processo pode levar algum tempo.

## Ideias e observações
- Utilizei a biblioteca multiprocessing para fazer a exploração dos repositórios com Beautiful Soup de forma assíncrona
- Não faz uso de bibliotecas para construir e imprimir a árvore de arquivos. Tudo é tratado pelo método recursivo explore_repository em scraper.py
- Realiza a contagem de bytes de arquivos que não possuam linhas de código
- Submódulos não são incluídos na árvore de arquivos

## Melhorias futuras
- Aplicar uma estrutura de árvore com pais e filhos, mantendo salvo o caminho das pastas e arquivos do repositório, e assim poder fazer a exploração das pastas e arquivos de forma assíncrona e consequentemente mais rápida
- Incluir submódulos encontrados no repositório no relatório
