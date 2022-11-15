import pytest
from django.urls import reverse
from rest_framework import status

from games.tests.client import GameAPIClient
from games.tests.factories import GameFactory, PlayerFactory


@pytest.mark.django_db
def test_join_game_after_game_room_full__with_computer_opponent():
    game = GameFactory(is_computer_opponent=True)
    PlayerFactory(game=game)

    payload = {
        "name": "KC",
    }

    client = GameAPIClient()
    url = reverse(client.join_url_name, args=[game.id])
    response = client.post(url, data=payload, format="json")

    assert response.status_code == status.HTTP_409_CONFLICT, response.json()

    assert response.json() == {'detail': 'The maximum allowed number of players have joined'}


@pytest.mark.django_db
def test_join_game_after_game_room_full__with_human_players_only():
    game = GameFactory(is_computer_opponent=False)
    PlayerFactory(game=game)
    PlayerFactory(game=game)

    payload = {
        "name": "KC",
    }

    client = GameAPIClient()
    url = reverse(client.join_url_name, args=[game.id])
    response = client.post(url, data=payload, format="json")

    assert response.status_code == status.HTTP_409_CONFLICT, response.json()

    assert response.json() == {'detail': 'The maximum allowed number of players have joined'}
