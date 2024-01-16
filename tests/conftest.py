# conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app
from .data_tests import user_data, boat_data, trip_data, booking_data, fishing_log_data

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
            pass

    # Surcharger la dépendance dans l'application FastAPI
    app.dependency_overrides[get_db] = override_get_db

    # Créer un TestClient en utilisant l'application surchargée
    with TestClient(app) as client:
        yield client

def create_user_and_token(client, user_data = user_data):    
    response = client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    user_id = response.json()["user_id"]

    response = client.post("/auth", json={
        "email": user_data["email"],
        "password": user_data["password"]
    })
    assert response.status_code == 200
    token = response.json()["access_token"]
    assert len(token) > 0

    return token, user_id

def create_boat(client, boat_data, user_data = user_data):
    token, user_id = create_user_and_token(client, user_data)
    
    boat_data["user_id"] = user_id
    
    reponse = client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert reponse.status_code == 200
    assert reponse.json()["name"] == boat_data["name"]
    
    boat_id = reponse.json()["boat_id"]
    return token, user_id, boat_id

def create_trip(client, trip_data = trip_data, user_data = user_data):
    token, user_id = create_user_and_token(client, user_data)
    
    trip_data["user_id"] = user_id
    
    reponse = client.post("/api/v1/trips/", json=trip_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert reponse.status_code == 200
    assert reponse.json()["title"] == trip_data["title"]
    
    trip_id = reponse.json()["trip_id"]
    return token, user_id, trip_id

def create_booking(client, booking_data = booking_data, trip_data = trip_data, user_data = user_data):
    token, user_id, trip_id = create_trip(client, trip_data, user_data)
    
    booking_data["user_id"] = user_id
    booking_data["trip_id"] = trip_id
    
    reponse = client.post("/api/v1/bookings/", json=booking_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert reponse.status_code == 200
    assert reponse.json()["name"] == booking_data["name"]
    
    booking_id = reponse.json()["booking_id"]
    return token, user_id, booking_id

def create_fishing_log(client, fishing_log_data = fishing_log_data, user_data = user_data):
    token, user_id = create_user_and_token(client, user_data)
    
    fishing_log_data["user_id"] = user_id
    fishing_log_data["boat_id"] = boat_id
    
    reponse = client.post("/api/v1/fishing_logs/", json=fishing_log_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert reponse.status_code == 200
    assert reponse.json()["name"] == fishing_log_data["name"]
    
    fishing_log_id = reponse.json()["fishing_log_id"]
    return token, user_id, fishing_log_id