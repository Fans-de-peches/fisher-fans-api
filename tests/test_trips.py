from app.main import app
from .conftest import test_client, create_user_and_token, create_boat
from .data_tests import user_data, user_2_data, trip_data, trip_2_data, boat_data, boat_2_data

def test_create_trip(test_client):
    token, boat_id, user_id = create_boat(test_client, boat_data, user_data)
    trip_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/trips/", json=trip_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["title"] == trip_data["title"]

def test_create_invalid_trip(test_client):
    token, boat_id, user_id = create_boat(test_client, boat_data, user_data)
    trip_data["user_id"] = user_id + 1
    
    response = test_client.post("/api/v1/trips/", json=trip_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_create_trip_not_logged(test_client):
    response = test_client.post("/api/v1/trips/", json=trip_data)
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"

def test_get_trips(test_client):
    token, boat_id, user_id = create_boat(test_client, boat_data, user_data)
    
    trip_data["user_id"] = user_id
    trip_2_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/trips/", json=trip_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["title"] == trip_data["title"]
    
    response = test_client.post("/api/v1/trips/", json=trip_2_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["title"] == trip_2_data["title"]

    response = test_client.get("/api/v1/trips/", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["total"] == 2
    assert response.json()["items"][0]["title"] == trip_data["title"]

def test_get_trip(test_client):
    token, boat_id, user_id = create_boat(test_client, boat_data, user_data)
    trip_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/trips/", json=trip_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["title"] == trip_data["title"]

    response = test_client.get("/api/v1/trips/" + str(response.json()["trip_id"]), headers={
        "Authorization": f"Bearer {token}"
    })

    assert response.status_code == 200
    assert response.json()["title"] == trip_data["title"]

def test_put_trip(test_client):
    token, boat_id, user_id = create_boat(test_client, boat_data, user_data)
    trip_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/trips/", json=trip_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["title"] == trip_data["title"]
    
    trip_2_data["user_id"] = user_id

    response = test_client.put("/api/v1/trips/" + str(response.json()["trip_id"]), json=trip_2_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["title"] == trip_2_data["title"]

def test_delete_trip(test_client):
    token, boat_id, user_id = create_boat(test_client, boat_data, user_data)
    trip_data["user_id"] = user_id
    
    response = test_client.post("/api/v1/trips/", json=trip_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["title"] == trip_data["title"]

    response = test_client.delete("/api/v1/trips/" + str(response.json()["trip_id"]), headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["message"] == "Trip deleted"

def test_delete_trip_not_found(test_client):
    token, boat_id, user_id = create_boat(test_client, boat_data, user_data)
    
    response = test_client.delete("/api/v1/trips/1", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 404
    assert response.json()["detail"] == "Trip not found"