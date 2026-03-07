def test_remove_participant_success(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 200
    # ensure participant was removed
    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]


def test_remove_nonexistent_activity_returns_404(client):
    # Act
    response = client.delete("/activities/NoneHere/participants?email=foo@bar.com")

    # Assert
    assert response.status_code == 404


def test_remove_not_signed_up_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "absent@x.com"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 400
