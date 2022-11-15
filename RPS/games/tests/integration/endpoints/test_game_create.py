import uuid
import pytest

from django.urls import reverse
from rest_framework import status

from games.tests.client import GameAPIClient


@pytest.mark.django_db
def test_create_new_game():
    test_game_id = str(uuid.uuid4())
    payload = {
        "game_id": test_game_id,
        "is_computer_opponent": True,
    }

    client = GameAPIClient()
    url = reverse(client.list_url_name)
    response = client.post(url, data=payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED, response.json()
    assert response.json()["game_id"] == test_game_id
