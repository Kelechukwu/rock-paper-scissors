import pytest

from django.urls import reverse
from rest_framework import status


from games.tests.client import GameAPIClient
from games.tests.factories import GameFactory, PlayerFactory
from games.enums import GameStatus


@pytest.mark.parametrize(
    "is_computer_opponent",
    (
        True,
        False,

    )
)
@pytest.mark.django_db
def test_start_game__check_required_players_joined(is_computer_opponent):
    game = GameFactory(is_computer_opponent=is_computer_opponent)
    PlayerFactory(game=game)

    payload = {
        "status": GameStatus.STARTED.name
    }

    client = GameAPIClient()
    url = reverse(client.detail_url_name, args=[game.id])
    response = client.patch(url, data=payload, format="json")


    if is_computer_opponent:
        expectation = status.HTTP_200_OK
    else:
        expectation = status.HTTP_409_CONFLICT

    assert response.status_code == expectation
