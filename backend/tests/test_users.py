from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

def test_get_current_user(client: TestClient, db: Session):
    client.post("/api/auth/register", json={
        "email": "test@example.com",
        "username": "testuser",
        "first_name": "Test",
        "last_name": "User",
        "password": "testpassword"
    })
    login_response = client.post("/api/auth/login", data={
        "username": "testuser",
        "password": "testpassword"
    })
    token = login_response.json()["access_token"]
    
    client.headers["Authorization"] = f"Bearer {token}"
    response = client.get("/api/users/me")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"