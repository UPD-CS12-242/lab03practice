import pytest

from model import SubtractASquareGame, Feedback


class TestInit:
    def test_n_invalid(self):
        invalid_ns = [0, -1, -2, -3, -4, -100]

        for n in invalid_ns:
            with pytest.raises(ValueError):
                SubtractASquareGame(n, 2)

    def test_player_count_invalid(self):
        invalid_player_counts = [1, 0, -1, -2, -3, -4, -100]

        for player_count in invalid_player_counts:
            with pytest.raises(ValueError):
                SubtractASquareGame(2, player_count)

    def test_both_invalid(self):
        invalid_ns = [0, -1, -2, -3, -4, -100]
        invalid_player_counts = [1, 0, -1, -2, -3, -4, -100]

        for n in invalid_ns:
            for player_count in invalid_player_counts:
                with pytest.raises(ValueError):
                    SubtractASquareGame(n, player_count)


class TestCurrentPlayer:
    def test_init_2(self):
        model = SubtractASquareGame(10, 2)
        assert model.current_player == 1

    def test_init_3(self):
        model = SubtractASquareGame(10, 3)
        assert model.current_player == 1

    def test_until_end_2(self):
        model = SubtractASquareGame(106, 2)
        assert model.current_player == 1

        model.subtract_square(64)
        assert model.current_player == 2

        model.subtract_square(1)
        assert model.current_player == 1

        model.subtract_square(36)
        assert model.current_player == 2

        model.subtract_square(4)
        assert model.current_player == 1

        model.subtract_square(1)
        assert model.current_player == 1

    def test_until_end_3(self):
        model = SubtractASquareGame(106, 3)
        assert model.current_player == 1

        model.subtract_square(64)
        assert model.current_player == 2

        model.subtract_square(1)
        assert model.current_player == 3

        model.subtract_square(36)
        assert model.current_player == 1

        model.subtract_square(4)
        assert model.current_player == 2

        model.subtract_square(1)
        assert model.current_player == 2


class TestPlayerCount:
    def test_2(self):
        model = SubtractASquareGame(10, 2)
        assert model.player_count == 2

    def test_3(self):
        model = SubtractASquareGame(10, 3)
        assert model.player_count == 3


class TestIsGameOver:
    def test_init(self):
        model = SubtractASquareGame(10, 2)
        assert not model.is_game_over

    def test_until_end_2(self):
        model = SubtractASquareGame(106, 2)
        assert not model.is_game_over

        model.subtract_square(64)
        assert not model.is_game_over

        model.subtract_square(1)
        assert not model.is_game_over

        model.subtract_square(36)
        assert not model.is_game_over

        model.subtract_square(4)
        assert not model.is_game_over

        model.subtract_square(1)
        assert model.is_game_over

    def test_until_end_3(self):
        model = SubtractASquareGame(106, 3)
        assert not model.is_game_over

        model.subtract_square(64)
        assert not model.is_game_over

        model.subtract_square(1)
        assert not model.is_game_over

        model.subtract_square(36)
        assert not model.is_game_over

        model.subtract_square(4)
        assert not model.is_game_over

        model.subtract_square(1)
        assert model.is_game_over


class TestN:
    def test_init_10(self):
        model = SubtractASquareGame(10, 2)
        assert model.n == 10

    def test_init_1(self):
        model = SubtractASquareGame(1, 2)
        assert model.n == 1


class TestSubtractSquare:
    def test_valid_16(self):
        model = SubtractASquareGame(100, 2)
        assert model.subtract_square(16) == Feedback.NEXT

    def test_invalid_square_greater(self):
        model = SubtractASquareGame(10, 2)
        assert model.subtract_square(16) == Feedback.GREATER_THAN_N

    def test_invalid_nonsquare_greater(self):
        model = SubtractASquareGame(10, 2)
        assert model.subtract_square(15) == Feedback.NOT_PERFECT_SQUARE

    def test_invalid_3(self):
        model = SubtractASquareGame(10, 2)
        assert model.subtract_square(3) == Feedback.NOT_PERFECT_SQUARE

    def test_valid_large(self):
        # Floats are imprecise for large values; refer to CS 136/138(?) (for why) and
        # https://stackoverflow.com/questions/2489435/check-if-a-number-is-a-perfect-square
        large_square = 152415789666209426002111556165263283035677489

        model = SubtractASquareGame(large_square + 1, 2)
        assert model.subtract_square(large_square) == Feedback.NEXT

    def test_invalid_large(self):
        large_nonsquare = 152415789666209426002111556165263283035677490

        model = SubtractASquareGame(large_nonsquare + 1, 2)
        assert model.subtract_square(
            large_nonsquare) == Feedback.NOT_PERFECT_SQUARE

    def test_invalid_0(self):
        model = SubtractASquareGame(10, 2)
        assert model.subtract_square(0) == Feedback.NOT_POSITIVE

    def test_invalid_neg_square_4(self):
        model = SubtractASquareGame(10, 2)
        assert model.subtract_square(-4) == Feedback.NOT_POSITIVE

    def test_invalid_neg_square_16(self):
        model = SubtractASquareGame(10, 2)
        assert model.subtract_square(-16) == Feedback.NOT_POSITIVE

    def test_invalid_neg_square_large(self):
        large_square = 152415789666209426002111556165263283035677489

        model = SubtractASquareGame(large_square, 2)
        assert model.subtract_square(-large_square) == Feedback.NOT_POSITIVE

    def test_until_end_2(self):
        model = SubtractASquareGame(106, 2)

        assert model.subtract_square(64) == Feedback.NEXT
        assert model.subtract_square(1) == Feedback.NEXT
        assert model.subtract_square(36) == Feedback.NEXT
        assert model.subtract_square(4) == Feedback.NEXT
        assert model.subtract_square(1) == Feedback.GAMEOVER

    def test_until_end_3(self):
        model = SubtractASquareGame(106, 3)

        assert model.subtract_square(64) == Feedback.NEXT
        assert model.subtract_square(1) == Feedback.NEXT
        assert model.subtract_square(36) == Feedback.NEXT
        assert model.subtract_square(4) == Feedback.NEXT
        assert model.subtract_square(1) == Feedback.GAMEOVER
