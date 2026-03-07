def test_signup_success_adds_participant(client):
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert "message" in body
    # participant list was updated
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    email = "michael@mergington.edu"  # already in initial participants
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400


def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    email = "foo@bar.com"
    activity = "Nonexistent"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404


def test_signup_capacity_enforced(client):
    # Arrange: fill an activity to capacity
    activity = "Tennis Club"
    info = client.get("/activities").json()[activity]
    current = len(info["participants"])
    cap = info["max_participants"]

    # add enough participants to reach capacity (if not already full)
    for i in range(cap - current):
        client.post(f"/activities/{activity}/signup?email=fill{i}@x.com")

    # Act: attempt one more signup
    response = client.post(f"/activities/{activity}/signup?email=overflow@x.com")

    # Assert
    assert response.status_code == 400
    assert "maximum capacity" in response.json().get("detail", "").lower()
