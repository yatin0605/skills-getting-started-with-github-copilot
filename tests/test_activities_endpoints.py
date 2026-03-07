def test_get_activities_structure(client):
    # Arrange: nothing special, client fixture provides a clean state

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # look for one known activity and verify its fields
    assert "Chess Club" in data
    example = data["Chess Club"]
    assert "description" in example
    assert "schedule" in example
    assert "max_participants" in example
    assert "participants" in example
