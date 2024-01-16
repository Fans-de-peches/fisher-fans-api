from app.main import app
from .conftest import test_client, create_user_and_token, create_trip, create_boat
from .data_tests import user_data, user_2_data, booking_data, booking_2_data, trip_data, trip_2_data, boat_data, boat_2_data

def test_create_booking(test_client):
    token, user_id, trip_id = create_trip(test_client, trip_data, user_data)
    boat_data["user_id"] = user_id
    reponse = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert reponse.status_code == 200
    
    booking_data["user_id"] = user_id
    booking_data["trip_id"] = trip_id
    
    response = test_client.post("/api/v1/bookings/", json=booking_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["date_dispo"] == booking_data["date_dispo"]

def test_get_bookings(test_client):
    token, user_id, trip_id = create_trip(test_client, trip_data, user_data)
    boat_data["user_id"] = user_id
    reponse = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert reponse.status_code == 200
    
    booking_data["user_id"] = user_id
    booking_data["trip_id"] = trip_id
    
    response = test_client.post("/api/v1/bookings/", json=booking_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["date_dispo"] == booking_data["date_dispo"]
    
    response = test_client.get("/api/v1/bookings/", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["total"] == 1
    assert response.json()["items"][0]["date_dispo"] == booking_data["date_dispo"]

def test_get_booking(test_client):
    token, user_id, trip_id = create_trip(test_client, trip_data, user_data)
    boat_data["user_id"] = user_id
    reponse = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert reponse.status_code == 200
    
    booking_data["user_id"] = user_id
    booking_data["trip_id"] = trip_id
    
    response = test_client.post("/api/v1/bookings/", json=booking_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["date_dispo"] == booking_data["date_dispo"]
    
    booking_id = response.json()["booking_id"]
    
    response = test_client.get(f"/api/v1/bookings/{booking_id}", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["date_dispo"] == booking_data["date_dispo"]

def test_get_user_bookings(test_client):
    token, user_id, trip_id = create_trip(test_client, trip_data, user_data)
    boat_data["user_id"] = user_id
    reponse = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert reponse.status_code == 200
    
    booking_data["user_id"] = user_id
    booking_data["trip_id"] = trip_id
    
    response = test_client.post("/api/v1/bookings/", json=booking_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["date_dispo"] == booking_data["date_dispo"]
    
    response = test_client.get(f"/api/v1/users/{user_id}/bookings", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["total"] == 1
    assert response.json()["items"][0]["date_dispo"] == booking_data["date_dispo"]

def test_put_booking(test_client):
    token, user_id, trip_id = create_trip(test_client, trip_data, user_data)
    boat_data["user_id"] = user_id
    reponse = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert reponse.status_code == 200
    
    booking_data["user_id"] = user_id
    booking_data["trip_id"] = trip_id
    
    response = test_client.post("/api/v1/bookings/", json=booking_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["date_dispo"] == booking_data["date_dispo"]
    
    booking_2_data["user_id"] = user_id
    booking_2_data["trip_id"] = trip_id

    booking_id = response.json()["booking_id"]

    response = test_client.put(f"/api/v1/bookings/{booking_id}", json=booking_2_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["date_dispo"] == booking_2_data["date_dispo"]

def test_delete_booking(test_client):
    token, user_id, trip_id = create_trip(test_client, trip_data, user_data)
    boat_data["user_id"] = user_id
    reponse = test_client.post("/api/v1/boats/", json=boat_data, headers={
        "Authorization": f"Bearer {token}"
    })
    assert reponse.status_code == 200
    
    booking_data["user_id"] = user_id
    booking_data["trip_id"] = trip_id
    
    response = test_client.post("/api/v1/bookings/", json=booking_data, headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["date_dispo"] == booking_data["date_dispo"]
    
    booking_id = response.json()["booking_id"]
    
    response = test_client.delete(f"/api/v1/bookings/{booking_id}", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    assert response.json()["message"] == "Booking deleted"