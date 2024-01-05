from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app  # Remplace par le chemin correct vers ton application FastAPI
from .conftest import test_client

user_data = {
    "first_name": "Jean",
    "last_name": "Dupont",
    "birth_date": "1990-01-01",
    "email": "jean.dupont@example.com",
    "mobile": "0612345678",
    "address": "123 Rue de la République",
    "zip_code": 75001,
    "city": "Paris",
    "languages": ["français", "anglais"],
    "avatar_url": "https://exemple.com/avatars/jeandupont.png",
    "boat_license_number": 123456,
    "insurance_number": "INS123456789",
    "status": "particulier",
    "company_name": None,
    "activity_type": None,
    "siret_number": None,
    "commerce_registry_number": None,
    "password": "unMotDePasseSécurisé123"
}

user2_data = {
    "first_name": "John",
    "last_name": "Doe",
    "birth_date": "2000-04-01",
    "email": "john.doe@exemple.com",
    "mobile": "0612345678",
    "address": "123 Rue de la République",
    "zip_code": 75001,
    "city": "Paris",
    "languages": ["français", "anglais"],
    "avatar_url": "https://exemple.com/avatars/johndoe.png",
    "boat_license_number": 123456,
    "insurance_number": "INS123456789",
    "status": "particulier",
    "company_name": None,
    "activity_type": None,
    "siret_number": None,
    "commerce_registry_number": None,
    "password": "unMotDePasseSécurisé123"
}

def test_create_user(test_client):
    response = test_client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]
# Autres assertions si nécessaire
def test_get_user(test_client):
    response = test_client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200

    response = test_client.get("/api/v1/users/" + str(response.json()["user_id"]))
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]

def test_get_users(test_client):
    response = test_client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    
    response = test_client.post("/api/v1/users/", json=user2_data)
    assert response.status_code == 200

    response = test_client.get("/api/v1/users/")
    assert response.status_code == 200
    assert response.json()["total"] == 2
    assert len(response.json()["items"]) == 2
    assert response.json()["items"][0]["email"] == user_data["email"]