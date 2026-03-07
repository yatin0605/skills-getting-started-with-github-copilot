import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

# keep a deep copy of the initial state so tests can reset it
_initial_activities = copy.deepcopy(activities)

@pytest.fixture
def client():
    """Return a TestClient for the FastAPI app."""
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities dictionary before each test."""
    activities.clear()
    activities.update(copy.deepcopy(_initial_activities))
    yield
    # after test, restore just in case
    activities.clear()
    activities.update(copy.deepcopy(_initial_activities))
