from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import models, schemas

def test_create_booking(client: TestClient, db: Session):
    # Setup user, hotel, and room
    user = models.User(
        email="user@example.com",
        username="user",
        first_name="Test",
        last_name="User",
        hashed_password="hashed_password"
    )
    hotel = models.Hotel(
        name="Test Hotel",
        address="123 Test St",
        city="Test City",
        country="Test Country",
        star_rating=4,
        phone="123-456-7890",
        email="test@hotel.com"
    )
    room = models.Room(
        hotel_id=1,
        room_number="101",
        room_type=models.RoomType.STANDARD,
        name="Standard Room",
        max_occupancy=2,
        base_price=100.0
    )
    db.add_all([user, hotel, room])
    db.commit()
    
    token = "test-token"  # Mock token
    client.headers["Authorization"] = f"Bearer {token}"
    
    response = client.post("/api/bookings/", json={
        "hotel_id": 1,
        "room_id": 1,
        "check_in_date": "2025-09-01T00:00:00",
        "check_out_date": "2025-09-03T00:00:00",
        "guests": 2,
        "special_requests": "None"
    })
    assert response.status_code == 200
    assert response.json()["booking_reference"]