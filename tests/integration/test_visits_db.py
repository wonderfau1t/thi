def test_first_request_uses_database(app_client):
    response = app_client.get("/visits")

    assert response.status_code == 200
    assert response.json()["source"] == "db"
    assert response.json()["count"] > 100
