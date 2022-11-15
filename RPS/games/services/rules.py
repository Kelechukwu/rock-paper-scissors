import random

from games.enums import Hand
from games.models import Game,Turn

RULE_GRAPH = {
    Hand.ROCK.name: {Hand.SCISSORS.name},
    Hand.SCISSORS.name: {Hand.PAPER.name},
    Hand.PAPER.name: {Hand.ROCK.name}
}


def get_turn(game_pk: int):
    game = Game.objects.filter(id=game_pk).first()

    if game:
        return game.turn


def switch_turns(game: Game):
    turn = Turn.objects.filter(game=game).first()
    current_player = turn.player

    other_player = game.players.exclude(id=current_player.id).first()

    if other_player:
        turn.player = other_player
        turn.save()
        return other_player

    # TODO: notify via pubsub instead
    return current_player


def set_initial_turn(game: Game):
    player_count = game.players.count()
    players = game.players.all()

    idx = random.randint(0, player_count - 1)

    new_turn = Turn(game=game, player=players[idx])
    new_turn.save()



def get_winning_hand(hand_1: Hand, hand_2: Hand):
    if hand_2 in RULE_GRAPH[hand_1]:
        return hand_1

    elif hand_1 in RULE_GRAPH[hand_2]:
        return hand_2
    
    # a draw 
    return None
  
