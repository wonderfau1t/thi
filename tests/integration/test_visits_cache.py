def test_second_request_uses_cache(app_client):
    app_client.get("/visits")
    response = app_client.get("/visits")

    assert response.json()["source"] == "cache"
