
from RPS.utils.misc import Conflict

from games.models import Game
from games.enums import GameStatus


def is_player_limit_reached(game: Game):
    players_count = game.players.count()

    single_player_limit_reached = players_count == 1 and game.is_computer_opponent
    multi_player_limit_reached = players_count == 2 and not game.is_computer_opponent

    return single_player_limit_reached or multi_player_limit_reached


def validate_players_count(game: Game):
    if is_player_limit_reached(game):
        raise Conflict("The maximum allowed number of players have joined")


def validate_game_can_be_played(game: Game):
    if not is_player_limit_reached(game):
        raise Conflict("Not all players have joined.")


def validate_game_status(game: Game):
    if game.status != GameStatus.STARTED.name:
        raise Conflict("The game has to be started first")

def validate_player_turn(game: Game, player_id):
    turn = game.turn

    if turn.player.id != player_id:
        raise Conflict("Please wait your turn")
