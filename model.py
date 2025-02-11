import math

from project_types import Feedback


class SubtractASquareGame:
    def __init__(self, n: int, player_count: int):
        if n <= 0:
            raise ValueError(f'n must be nonnegative (was {n})')

        if player_count <= 1:
            raise ValueError(f'n must be at least 2 (was {player_count})')

        self._player_count = player_count
        self._current_player = 1
        self._n = n

    @property
    def current_player(self):
        return self._current_player

    @property
    def player_count(self):
        return self._player_count

    @property
    def is_game_over(self):
        return self.n == 0

    @property
    def n(self):
        return self._n

    @property
    def _next_player(self):
        return (self._current_player % self.player_count) + 1

    def _switch_to_next_player(self):
        self._current_player = self._next_player

    def _subtract_from_n(self, k: int):
        self._n -= k

    def subtract_square(self, k: int) -> Feedback:
        if k <= 0:
            return Feedback.NOT_POSITIVE

        if not self._is_perfect_square(k):
            return Feedback.NOT_PERFECT_SQUARE

        if k > self.n:
            return Feedback.GREATER_THAN_N

        self._subtract_from_n(k)

        if self.is_game_over:
            return Feedback.GAMEOVER

        self._switch_to_next_player()

        return Feedback.NEXT

    def _is_perfect_square(self, n: int):
        return math.isqrt(n) ** 2 == n
