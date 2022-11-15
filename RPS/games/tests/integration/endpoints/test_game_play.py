import pytest
from django.urls import reverse
from rest_framework import status

from games.tests.client import GameAPIClient
from games.tests.factories import GameFactory, PlayerFactory, TurnFactory
from games.enums import Hand, GameStatus


@pytest.mark.parametrize(
    "computer_hand, player_hand, expected_winner",
    (
        (Hand.ROCK.name, Hand.PAPER.name, "player"),
        (Hand.PAPER.name, Hand.SCISSORS.name, "player"),
        (Hand.ROCK.name, Hand.SCISSORS.name, "computer"),

        (Hand.ROCK.name, Hand.ROCK.name, "draw"),
        (Hand.PAPER.name, Hand.PAPER.name, "draw"),
        (Hand.SCISSORS.name, Hand.SCISSORS.name, "draw"),


    )
)
@pytest.mark.django_db
def test_game_play__against_computer(
        mocker, computer_hand, player_hand, expected_winner):
    mocker.patch("games.services.play._get_computer_hand",
                 return_value=computer_hand)
    game = GameFactory(is_computer_opponent=True, status=GameStatus.STARTED.name)
    player = PlayerFactory(game=game)

    TurnFactory(player=player, game=game)

    payload = {
        "player_id": player.id,
        "hand": player_hand
    }

    client = GameAPIClient()
    url = reverse(client.play_url_name, args=[game.id])
    response = client.post(url, data=payload, format="json")

    response_json = response.json()

    assert expected_winner in response_json["outcome"].lower()
    if expected_winner == "player":
        player.wins = 1

    if expected_winner == "draw":
        player.draws = 1

