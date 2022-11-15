from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import status

from games.models import Game
from games.enums import GameStatus
from games.serializers import GameSerializer, PlayerSerializer, PlaySerializer
from games.services.validations import validate_players_count, validate_game_can_be_played, validate_player_turn, validate_game_status
from games.services.rules import set_initial_turn, switch_turns
from games.data_initialisers import PlayerDataInitialiser
from games.services.play import play_game



class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_update(self, serializer):
        data = self.request.data
        if data.get("status") == GameStatus.STARTED.name:
            game = self.get_object()
            validate_game_can_be_played(game)

        super().perform_update(serializer)

        # Set turn 
        set_initial_turn(self.get_object())


    @action(detail=True, methods=["POST"])
    def join(self, request, *args, **kwargs):
        game = self.get_object()

        # check number of players 
        validate_players_count(game)

        # prepare payload that links player to a game
        data_initialiser = PlayerDataInitialiser(request)
        data_initialiser.initialise(game)

        # validation
        serializer = PlayerSerializer(data=data_initialiser.data)
        serializer.is_valid(raise_exception=True)

        new_player  = serializer.save()
        new_player_serializer = PlayerSerializer(instance=new_player)

        return Response(new_player_serializer.data,
                        status=status.HTTP_201_CREATED)


    @action(detail=True, methods=["POST"])
    def play(self, request, *args, **kwargs):
        game = self.get_object()

        # validate the game status
        validate_game_status(game)

        # validate the payload
        serializer = PlaySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        player_id = serializer.data.get("player_id")
        hand = serializer.data.get("hand")

        validate_player_turn(game, player_id)

        outcome = play_game(game, player_id, hand)

        switch_turns(game)

        return Response({"outcome": outcome}, status=status.HTTP_200_OK)
