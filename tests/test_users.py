from app.main import app
from .conftest import test_client, create_user_and_token
from .data_tests import user_data, user_2_data, boat_data, boat_2_data

def test_create_user(test_client):
    response = test_client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]

def test_get_user(test_client):
    token, user_id = create_user_and_token(test_client, user_data)

    response = test_client.get("/api/v1/users/" + str(user_id), headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]

def test_get_users(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    
    response = test_client.post("/api/v1/users/", json=user_2_data)
    assert response.status_code == 200
    
    response = test_client.get("/api/v1/users/", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["total"] == 2
    assert len(response.json()["items"]) == 2
    assert response.json()["items"][0]["email"] == user_data["email"]

def test_get_current_user(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
        
    response = test_client.get("/api/v1/users/me", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]

def test_get_user_lists(test_client):
    token, user_id = create_user_and_token(test_client, user_data)        
    boat_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["name"] == boat_data["name"]

    response = test_client.get("/api/v1/users/"+ str(user_id) + "/boats/", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()['total'] == 1
    assert response.json()['items'][0]["name"] == boat_data["name"]

def test_update_user(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    
    user_data["first_name"] = "John"
    user_data["password"] = None
    
    response = test_client.put("/api/v1/users/" + str(user_id), json=user_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["first_name"] == "John"