def test_register_user(client):
    response = client.post(
        "/users/register",
        json={"email": "pytest@example.com", "password": "testpassword123"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "pytest@example.com"
    assert "id" in data


def test_login_and_get_me(client):
    # 1. Register a user
    client.post(
        "/users/register",
        json={"email": "pytest@example.com", "password": "testpassword123"}
    )

    # 2. Log in
    login_res = client.post(
        "/users/login",
        data={"username": "pytest@example.com", "password": "testpassword123"}
    )
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]

    # 3. Request /users/me using the Bearer token header
    headers = {"Authorization": f"Bearer {token}"}
    me_res = client.get("/users/me", headers=headers)
    
    assert me_res.status_code == 200
    assert me_res.json()["email"] == "pytest@example.com"


def test_unauthorized_access(client):
    # Trying to access protected route without token should return 401
    response = client.get("/users/me")
    assert response.status_code == 401