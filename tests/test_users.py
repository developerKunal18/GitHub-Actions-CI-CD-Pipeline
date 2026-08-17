def test_create_user(client):
    response = client.post("/users", json={
        "name": "Kunal",
        "email": "kunal@example.com"
    })
    assert response.status_code == 201
    assert response.json["name"] == "Kunal"

def test_missing_name(client):
    response = client.post("/users", json={
        "email": "kunal@example.com"
    })
    assert response.status_code == 400
    assert response.json["error"] == "Name required"

def test_duplicate_email(client):
    payload = {"name": "Kunal", "email": "kunal@example.com"}
    first = client.post("/users", json=payload)
    second = client.post("/users", json=payload)
    assert first.status_code == 201
    assert second.status_code == 409
