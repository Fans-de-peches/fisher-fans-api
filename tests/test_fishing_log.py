from app.main import app
from .conftest import test_client, create_user_and_token
from .data_tests import user_data, user_2_data, fishing_log_data, fishing_log_2_data

def test_create_fishing_log(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    fishing_log_data["user_id"] = user_id

    response = test_client.post("/api/v1/logs/", json=fishing_log_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["fish_name"] == fishing_log_data["fish_name"]

def get_fishing_logs(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    fishing_log_data["user_id"] = user_id

    response = test_client.post("/api/v1/logs/", json=fishing_log_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["fish_name"] == fishing_log_data["fish_name"]
    
    fishing_log_2_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/logs/", json=fishing_log_2_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["fish_name"] == fishing_log_2_data["fish_name"]

    response = test_client.get("/api/v1/logs/", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()['total'] == 2
    assert response.json()['items'][0]["fish_name"] == fishing_log_data["fish_name"]

def test_get_fishing_log(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    fishing_log_data["user_id"] = user_id

    response = test_client.post("/api/v1/logs/", json=fishing_log_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["fish_name"] == fishing_log_data["fish_name"]
    log_id = response.json()["log_id"]

    response = test_client.get("/api/v1/logs/" + str(log_id), headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["fish_name"] == fishing_log_data["fish_name"]

def test_update_fishing_log(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    fishing_log_data["user_id"] = user_id

    response = test_client.post("/api/v1/logs/", json=fishing_log_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["fish_name"] == fishing_log_data["fish_name"]
    log_id = response.json()["log_id"]

    fishing_log_data["fish_name"] = "Nouveau nom du poisson"

    response = test_client.put("/api/v1/logs/" + str(log_id), json=fishing_log_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["fish_name"] == fishing_log_data["fish_name"]

def test_delete_fishing_log(test_client):
    token, user_id = create_user_and_token(test_client, user_data)
    fishing_log_data["user_id"] = user_id

    response = test_client.post("/api/v1/logs/", json=fishing_log_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["fish_name"] == fishing_log_data["fish_name"]
    log_id = response.json()["log_id"]

    response = test_client.delete("/api/v1/logs/" + str(log_id), headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Log deleted"