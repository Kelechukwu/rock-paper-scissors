class PlayerDataInitialiser:
    def __init__(self, request) -> None:
        self.data = request.data or {}

    def initialise(self, game):
        self.data["game"] = game.id

