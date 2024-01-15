from app.main import app
from .conftest import test_client, create_user_and_token
from .data_tests import user_data, user_2_data, boat_data, boat_2_data

def test_create_boat(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    boat_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["name"] == boat_data["name"]

def test_get_boats(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    
    boat_data["user_id"] = user_id
    boat_2_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["name"] == boat_data["name"]
    
    response = test_client.post("/api/v1/boats/", json=boat_2_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["name"] == boat_2_data["name"]

    response = test_client.get("/api/v1/boats/", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["total"] == 2
    assert response.json()["items"][0]["name"] == boat_data["name"]

def test_get_boat(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    boat_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["name"] == boat_data["name"]

    response = test_client.get("/api/v1/boats/" + str(response.json()["boat_id"]), headers={
        "Authorization": f"Bearer {token}"
    })

    assert response.status_code == 200
    assert response.json()["name"] == boat_data["name"]

def test_get_boats_by_zone(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    
    boat_data["user_id"] = user_id
    boat_2_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["name"] == boat_data["name"]
    
    response = test_client.post("/api/v1/boats/", json=boat_2_data, headers={
        "Authorization": f"Bearer {token}"  
    })
    assert response.status_code == 200
    assert response.json()["name"] == boat_2_data["name"]

    response = test_client.get("/api/v1/boats/search_zone?x_min=0&x_max=10&y_min=0&y_max=50", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["total"] == 1
    assert response.json()["items"][0]["name"] == boat_data["name"]

def test_update_boat(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    boat_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["name"] == boat_data["name"]
    
    boat_data["name"] = "Nouveaux nom"
    boat_data["birth_date"] = None

    response = test_client.put("/api/v1/boats/" + str(response.json()["boat_id"]), json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["name"] == boat_data["name"]