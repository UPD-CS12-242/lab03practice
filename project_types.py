from enum import Enum, auto


class Feedback(Enum):
    NEXT = auto()
    GAMEOVER = auto()
    NOT_PERFECT_SQUARE = auto()
    GREATER_THAN_N = auto()
    NOT_POSITIVE = auto()
