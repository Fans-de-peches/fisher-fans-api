# Fisher Fans API

## Description

Fisher Fans API est une plateforme innovante conçue pour connecter les passionnés de pêche. Elle permet aux utilisateurs de gérer leurs sorties de pêche, de réserver des bateaux et de suivre leurs prises, le tout à partir d'une interface simple et intuitive.

## Commencer

Ces instructions vous aideront à configurer le projet pour le développement et les tests.

### Prérequis

- Python 3.8+
- pip

### Installation

Clonez le projet, créez un environnement virtuel et installez les dépendances :

```bash
git clone https://github.com/Fans-de-peches/fisher-fans-api.git
cd fisher-fans-api
python -m venv fisher_env
# Unix ou MacOS
source fisher_env/bin/activate
# Windows
fisher_env\Scripts\activate
pip install -r requirements.txt
```

### Exécution

Pour lancer le serveur :

```bash
# En HTTP
uvicorn app.main:app --reload
# En HTTPS (nécessite des certificats SSL)
uvicorn app.main:app --reload --ssl-keyfile=./path-to-key.pem --ssl-certfile=./path-to-cert.pem
```

### Exécution des Tests

Exécutez les tests avec pytest :

```bash
pytest
```

## Création de Certificats SSL avec mkcert

Pour sécuriser votre API en local avec HTTPS, vous pouvez créer des certificats SSL en utilisant mkcert. Suivez ces étapes :

1. **Installer mkcert** :
   - Installez mkcert sur votre système. Pour les instructions spécifiques à votre OS, consultez [la documentation mkcert](https://github.com/FiloSottile/mkcert).

2. **Créer un Certificat Local** :
   - Exécutez `mkcert -install` pour installer une autorité de certification locale.
   - Créez un certificat pour votre domaine local (par exemple, `localhost`) avec `mkcert localhost`.

3. **Configurer le Serveur** :
   - Utilisez les fichiers de certificat générés pour configurer votre serveur (par exemple, uvicorn) avec HTTPS.

Cette méthode vous permet de tester votre application en local avec une connexion HTTPS sécurisée.

## Construit Avec

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [python-jose](https://python-jose.readthedocs.io/en/latest/)
- [passlib](https://passlib.readthedocs.io/en/stable/)
- [pytest](https://docs.pytest.org/en/stable/)

## Auteurs

- **Matisse Moni** - [Github](https://github.com/MatisseMoni)
- **Gabriel Rivas** - [Github](https://github.com/RivasGabriel)
- **Winston Pelletier** - [Github](https://github.com/Ninwost)
- **Julien Pessione** - [Github](https://github.com/PessioneJulien)

---