# fisher-fans-api

Une brève description de ce que fait ton projet.

## Description

Fournis une description plus détaillée de ton projet. Explique ce que fait ton API, pourquoi elle a été créée, et quels problèmes elle résout.

## Commencer

Ces instructions te permettront d'obtenir une copie du projet en cours d'exécution sur ta machine locale à des fins de développement et de test.

### Prérequis

Python 3.8
pip

### Installation

`$ git clone https://github.com/Fans-de-peches/fisher-fans-api.git`
`$ cd fisher-fans-api`
`$ python -m venv fisher_env`
`$ source fisher_env/bin/activate` (pour Unix ou MacOS) ou `fisher_env\Scripts\activate` (pour Windows)
`$ pip install -r requirements.txt`

### Exécution
`.\fisher_env\Scripts\activate`

Executé en http
`$ uvicorn app.main:app --reload`
Executé en https (nécessite la génération des certificats ssl)
`$ uvicorn app.main:app --reload --ssl-keyfile=./127.0.0.1+1-key.pem --ssl-certfile=./127.0.0.1+1.pem`

### Exécution des tests

`$ pytest`

## Construit avec

* [FastAPI](https://fastapi.tiangolo.com/) - Le framework web utilisé
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM et gestionnaire de base de données
* [SQLite](https://www.sqlite.org/index.html) - Base de données utilisée
* [Pydantic](https://pydantic-docs.helpmanual.io/) - Gestion de la validation des données
* [python-jose](https://python-jose.readthedocs.io/en/latest/) - Authentification JWT
* [pytest](https://docs.pytest.org/en/stable/) - Framework de test

## Auteurs

* **Matisse Moni** - *Travail Initial* - [Github](https://github.com/MatisseMoni)
* **Gabriel Rivas** - *Documentation* - [Github](https://github.com/RivasGabriel)
* **Winston Pelletier** - *Documentation* - [Github](https://github.com/Ninwost)
* **Julien Pessione** - *Documentation* - [Github](https://github.com/PessioneJulien)