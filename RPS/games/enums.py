from enum import IntEnum, unique


@unique
class Hand(IntEnum):
    ROCK=0
    PAPER=1
    SCISSORS=2

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


@unique
class GameStatus(IntEnum):
    PENDING = 0
    STARTED = 1
    PAUSED = 2

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
