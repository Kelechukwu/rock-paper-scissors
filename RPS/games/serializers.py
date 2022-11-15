from rest_framework import serializers
from games.models import Game, Player, Turn
from games.enums import Hand


class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    turn = TurnSerializer(required=False)
    class Meta:
        model = Game
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlaySerializer(serializers.Serializer):
    player_id = serializers.IntegerField()
    hand = serializers.ChoiceField(choices=Hand.choices())
