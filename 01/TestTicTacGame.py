import unittest
from TicTac import TicTacGame


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame(3)

    def test_check_winner(self):
        self.game.winner = "X"
        self.assertEqual(self.game._check_winner(), "X")
        self.game.winner = ""
        self.assertEqual(self.game._check_winner(), None)
        self.game.winner = "O"
        self.assertEqual(self.game._check_winner(), "O")

    def test_tracking_moves(self):
        self.game.move_tracking = [0] * (len(self.game.board) * 2 + 2)

        self.game._fill_tracking_move(0, 0, "X")
        self.assertEqual(self.game.move_tracking,[1, 0, 0, 1, 0, 0, 1, 0])

        self.game._fill_tracking_move(1, 2, "O")
        self.assertEqual(self.game.move_tracking, [1, 0, -1, 1, -1, 0, 1, 0])

        self.game._fill_tracking_move(2, 2, "X")
        self.assertEqual(self.game.move_tracking, [1, 0, 0, 1, -1, 1, 2, 0])

        self.game._fill_tracking_move(1, 1, "X")
        self.assertEqual(self.game.move_tracking, [1, 1, 0, 1, 0, 1, 3, 1])

    def test_tracking_winner(self):
        self.game.move_tracking = [1, 0, 0, 1, -1, 1, 2, 0]
        self.game._fill_tracking_move(1, 1, "X")
        self.assertEqual(self.game.winner, "X")

        self.game.move_tracking = [-1, 0, 1, -1, 2, -1, 1, 1]
        self.game._fill_tracking_move(2, 0, "X")
        self.assertEqual(self.game.winner, "X")

        self.game.move_tracking = [0, -1, 1, 2, -1, -1, -2, -1]
        self.game._fill_tracking_move(2, 0, "O")
