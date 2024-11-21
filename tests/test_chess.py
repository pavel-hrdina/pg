import unittest

from chess import Pawn, Knight, Bishop, Rook, Queen, King


class TestChessPieces(unittest.TestCase):
    def setUp(self):
        self.white_pawn = Pawn("white", (2, 2))
        self.black_pawn = Pawn("black", (7, 2))
        self.knight = Knight("white", (4, 4))
        self.bishop = Bishop("black", (4, 4))
        self.rook = Rook("white", (4, 4))
        self.queen = Queen("black", (4, 4))
        self.king = King("white", (4, 4))

    def test_pawn_moves(self):
        self.assertEqual(self.white_pawn.possible_moves(), [(3, 2)])
        self.assertEqual(self.black_pawn.possible_moves(), [(6, 2)])

    def test_knight_moves(self):
        self.assertEqual(
            set(self.knight.possible_moves()),
            {(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)},
        )

    def test_bishop_moves(self):
        self.assertEqual(
            set(self.bishop.possible_moves()),
            {
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (3, 3),
                (2, 2),
                (1, 1),
                (5, 3),
                (6, 2),
                (7, 1),
                (3, 5),
                (2, 6),
                (1, 7),
            },
        )

    def test_rook_moves(self):
        self.assertEqual(
            set(self.rook.possible_moves()),
            {
                (4, 1),
                (4, 2),
                (4, 3),
                (4, 5),
                (4, 6),
                (4, 7),
                (4, 8),
                (1, 4),
                (2, 4),
                (3, 4),
                (5, 4),
                (6, 4),
                (7, 4),
                (8, 4),
            },
        )

    def test_queen_moves(self):
        self.assertEqual(
            set(self.queen.possible_moves()),
            {
                (5, 5),
                (3, 3),
                (5, 3),
                (3, 5),
                (4, 1),
                (1, 4),
                (6, 6),
                (2, 2),
                (6, 2),
                (2, 6),
                (4, 2),
                (2, 4),
                (7, 7),
                (1, 1),
                (7, 1),
                (1, 7),
                (4, 3),
                (3, 4),
                (8, 8),
                (4, 4),
                (4, 4),
                (4, 5),
                (5, 4),
                (4, 6),
                (6, 4),
                (4, 7),
                (7, 4),
                (4, 8),
                (8, 4),
            },
        )

    def test_king_moves(self):
        self.assertEqual(
            set(self.king.possible_moves()),
            {
                (3, 3),
                (3, 4),
                (3, 5),
                (4, 3),
                (4, 5),
                (5, 3),
                (5, 4),
                (5, 5),
            },
        )


if __name__ == "__main__":
    unittest.main()
