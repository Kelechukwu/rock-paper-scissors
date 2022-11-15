import pytest
from django.urls import reverse
from rest_framework import status

from games.tests.client import GameAPIClient
from games.tests.factories import GameFactory


@pytest.mark.django_db
def test_join_game_as_first_player():
    game = GameFactory()
    payload = {
        "name": "KC",
    }

    client = GameAPIClient()
    url = reverse(client.join_url_name, args=[game.id])
    response = client.post(url, data=payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED, response.json()

