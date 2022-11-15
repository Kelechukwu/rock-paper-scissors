from django.db import models
from games.enums import GameStatus, Hand


class Game(models.Model):
    game_id = models.UUIDField(db_index=True)
    is_computer_opponent = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=GameStatus.choices(), default=GameStatus.PENDING)


class Player(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    game = models.ForeignKey(
        Game, related_name="players", on_delete=models.CASCADE)
    played = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    draws = models.PositiveSmallIntegerField(default=0)
    hand = models.CharField(
        max_length=255, choices=Hand.choices(),
        null=True)


class Turn(models.Model):
    game = models.OneToOneField(
        Game, related_name="turn", on_delete=models.CASCADE)
    player = models.ForeignKey(
        Player, related_name="player_turn", on_delete=models.CASCADE)


