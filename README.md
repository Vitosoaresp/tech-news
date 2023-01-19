# Tech News

 O principal objetivo desse projeto é fazer raspagem em notícias sobre tecnologia. Noticias que são retidaras do [blog da Trybe](https://blog.betrybe.com/)
 
 ![image](https://user-images.githubusercontent.com/23152592/213334703-5a5f80c7-c3bd-444b-845e-a802784f30ee.png)

 
# Tecnologias
 
 > Desenvolvindo usando: [Python](https://www.python.org/), [Docker](https://www.docker.com/), [MongoDB](https://www.mongodb.com/pt-br), [Pymongo](https://pymongo.readthedocs.io/en/stable/)
 
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
 ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
 
 # Como rodar o projeto
 
1 - Clone o repositório
    
    git clone git@github.com:Vitosoaresp/tech-news.git

2 - Crie ambiente virtual e instale as dependências

    cd tech-news/
    python3 -m venv .venv && source .venv/bin/activate
    python3 -m pip install -r dev-requirements.txt
    
3 - Rode o banco de dados via docker

    docker-compose up -d mongodb

 ## Analyzer Menu
 
    Selecione uma das opções a seguir:
    
     0 - Popular o banco com notícias;
     1 - Buscar notícias por título;
     2 - Buscar notícias por data;
     3 - Buscar notícias por tag;
     4 - Buscar notícias por categoria;
     5 - Listar top 5 notícias;
     6 - Listar top 5 categorias;
     7 - Sair.
        
 ![image](https://user-images.githubusercontent.com/23152592/213333596-fe34c7dd-616a-4dae-a8b6-b4c232eb33ca.png)

```bash
python3 tech_news/menu.py
```

> Lembre-se de popular o banco primeiro.

## Arquivos desenvolvidos por mim

       tech-news/menu.py
       tech-news/scraper.py
       tech-news/analyzer/ratings.py
       tech-news/analyzer/search_engine.py
    
 ## Arquivos desenvolvidos pela trybe
 
       tech-news/database.py
       tests/
       Dockerfile
       docker-compose.yml
       dev-requeriments.txt
       requeriments.txt
       setup.*
       pyproject.toml
