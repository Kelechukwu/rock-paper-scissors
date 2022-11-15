import random

from games.enums import Hand
from games.models import Game, Player
from games.services.rules import RULE_GRAPH, get_winning_hand


def _get_computer_hand():
    options = list(RULE_GRAPH.keys())

    options_count = len(RULE_GRAPH)

    idx = random.randint(0, options_count - 1)

    return options[idx]


def _save_player_hand(player_id: int, player_hand: Hand):
    player = Player.objects.filter(id=player_id).first()
    player.hand = player_hand
    player.played += 1
    player.save()

    return player


def _increment_wins(player: Player):
    player.wins += 1
    player.save()

def _increment_draws(player: Player):
    player.draws += 1
    player.save()


def play_game(game: Game, player_id: int, player_hand: Hand):
    player = _save_player_hand(player_id, player_hand)

    if game.is_computer_opponent:
        computer_hand = _get_computer_hand()

        winning_hand = get_winning_hand(player_hand, computer_hand)

        if player.hand == computer_hand:
            return "DRAW"

        if player.hand == winning_hand:
            _increment_wins(player)
            return player.name
        
        return "COMPUTER"

    other_player = game.players.exclude(id=player_id.id).first()
    should_check_for_winner = player.played == other_player.played

    if should_check_for_winner:
        winning_hand = get_winning_hand(player_hand, other_player.hand)

        if player.hand == other_player.hand:
            _increment_draws(player)
            _increment_draws(other_player)
            return "DRAW"

        if player.hand == winning_hand:
            _increment_wins(player)
            return player.name
    
        _increment_wins(other_player)
        return other_player.name

