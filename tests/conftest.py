# conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db  # Assure-toi d'importer la base de données correctement
from app.main import app
# Configuration pour la base de données de test
SQLALCHEMY_DATABASE_URL = "sqlite:///./tests/test_database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def db_engine():
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def test_client(db_session):
    # Fonction pour surcharger get_db
    def override_get_db():
        try:
            yield db_session
        finally:
            pass  # La session est nettoyée par la fixture db_session

    # Surcharger la dépendance dans l'application FastAPI
    app.dependency_overrides[get_db] = override_get_db

    # Créer un TestClient en utilisant l'application surchargée
    with TestClient(app) as client:
        yield client
