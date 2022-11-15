import pytest

from django.urls import reverse
from rest_framework import status

from games.tests.client import GameAPIClient
from games.tests.factories import GameFactory, PlayerFactory
from games.enums import GameStatus


@pytest.mark.django_db
def test_start_game():
    game = GameFactory(is_computer_opponent=True)
    player  = PlayerFactory(game=game)

    payload = {
        "status": GameStatus.STARTED.name
    }


    client = GameAPIClient()
    url = reverse(client.detail_url_name, args=[game.id])
    response = client.patch(url, data=payload, format="json")

    assert response.status_code == status.HTTP_200_OK, response.json()

    response_json  = response.json()
    assert response_json["status"] == "STARTED"
    assert response_json["turn"]["player"] == player.id

