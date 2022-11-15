from rest_framework.test import APIClient


class GameAPIClient(APIClient):
    list_url_name = "game-list"
    detail_url_name = "game-detail"
    join_url_name = "game-join"
    play_url_name = "game-play"

