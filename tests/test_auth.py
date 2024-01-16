from app.main import app
from .conftest import test_client
from .data_tests import user_data, user_2_data, boat_data, boat_2_data

def test_create_token(test_client):
    response = test_client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    
    response = test_client.post("/auth", json={
        "email": user_data["email"],
        "password": user_data["password"]
    })
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert len(response.json()["access_token"]) > 0

def test_create_token_invalid_credentials(test_client):
    response = test_client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    
    response = test_client.post("/auth", json={
        "email": user_data["email"],
        "password": "invalid_password"
    })
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect email or password"

def test_refresh_token(test_client):
    response = test_client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    
    response = test_client.post("/auth", json={
        "email": user_data["email"],
        "password": user_data["password"]
    })
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert len(response.json()["access_token"]) > 0
    
    response = test_client.post("/auth/refresh", headers={
        "Authorization": "Bearer " + response.json()["access_token"]
    })
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert len(response.json()["access_token"]) > 0

def test_refresh_token_invalid_credentials(test_client):
    response = test_client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    
    response = test_client.post("/auth", json={
        "email": user_data["email"],
        "password": user_data["password"]
    })
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert len(response.json()["access_token"]) > 0
    
    response = test_client.post("/auth/refresh", headers={
        "Authorization": "Bearer " + response.json()["access_token"] + "invalid"
    })
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"