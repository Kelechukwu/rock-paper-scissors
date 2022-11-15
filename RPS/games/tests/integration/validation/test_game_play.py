import pytest
from django.urls import reverse
from rest_framework import status

from games.tests.client import GameAPIClient
from games.tests.factories import GameFactory, PlayerFactory, TurnFactory
from games.enums import Hand, GameStatus


@pytest.mark.parametrize(
    "game_status, is_allowed",
    (
        (GameStatus.STARTED.name, True),
        (GameStatus.PENDING.name, False),
        (GameStatus.PAUSED.name, False),

    )
)
@pytest.mark.django_db
def test_play_game__check_status(game_status, is_allowed):
    game = GameFactory(is_computer_opponent=True, status=game_status)
    player = PlayerFactory(game=game)

    TurnFactory(player=player, game=game)

    payload = {
        "player_id": player.id,
        "hand": Hand.ROCK.name
    }

    client = GameAPIClient()
    url = reverse(client.play_url_name, args=[game.id])
    response = client.post(url, data=payload, format="json")

    if is_allowed:
        assert response.status_code == status.HTTP_200_OK, response.json()

    else:
        assert response.status_code == status.HTTP_409_CONFLICT, response.json()
        assert response.json() == {'detail': 'The game has to be started first'}


@pytest.mark.django_db
def test_play_game__check_turn():
    game = GameFactory(status=GameStatus.STARTED.name)
    player_1 = PlayerFactory(game=game)
    player_2 = PlayerFactory(game=game)

    TurnFactory(player=player_1, game=game)

    payload = {
        "player_id": player_2.id,
        "hand": Hand.ROCK.name
    }

    client = GameAPIClient()
    url = reverse(client.play_url_name, args=[game.id])
    response = client.post(url, data=payload, format="json")


    assert response.status_code == status.HTTP_409_CONFLICT, response.json()
    assert response.json() == {'detail': 'Please wait your turn'}
