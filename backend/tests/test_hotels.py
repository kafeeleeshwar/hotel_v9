from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import models, schemas

def test_create_hotel(client: TestClient, db: Session):
    # Create admin user for authentication
    admin = models.User(
        email="admin@example.com",
        username="admin",
        first_name="Admin",
        last_name="User",
        hashed_password="hashed_password",
        role=models.UserRole.ADMIN
    )
    db.add(admin)
    db.commit()
    
    token = "test-token"  # Mock token for simplicity
    client.headers["Authorization"] = f"Bearer {token}"
    
    response = client.post("/api/hotels/", json={
        "name": "Test Hotel",
        "description": "A test hotel",
        "address": "123 Test St",
        "city": "Test City",
        "country": "Test Country",
        "star_rating": 4,
        "phone": "123-456-7890",
        "email": "test@hotel.com",
        "latitude": 40.0,
        "longitude": -74.0
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Hotel"