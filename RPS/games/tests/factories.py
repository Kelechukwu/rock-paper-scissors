import uuid

import factory
from factory.django import DjangoModelFactory

from games.models import Game, Player, Turn

class GameFactory(DjangoModelFactory):
    game_id = factory.Sequence(lambda i: uuid.uuid4())
    is_computer_opponent = False

    class Meta:
        model = Game


class PlayerFactory(DjangoModelFactory):
    name = factory.Sequence(lambda i: f"Player-{i}")
    game = factory.SubFactory(GameFactory)
    wins = 0
    draws = 0

    class Meta:
        model = Player


class TurnFactory(DjangoModelFactory):
    game = factory.SubFactory(GameFactory)
    player = factory.SubFactory(PlayerFactory)

    class Meta:
        model = Turn
