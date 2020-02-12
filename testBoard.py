import unittest
from playToken import PlayToken
from tictactoe import Board

class TestBoardMarkBoard(unittest.TestCase):

    def setUp(self):
        self.b = Board()

    def test_markBoardSuccess(self):
        self.assertTrue(self.b.mark_square(1, 1, PlayToken.X))

    def test_markBoardLocationCheck(self):
        self.b.mark_square(1, 1, PlayToken.X)
        self.assertEqual(self.b.tictactoeBoard, [PlayToken.E, PlayToken.E, PlayToken.E,
                                            PlayToken.E, PlayToken.X, PlayToken.E,
                                            PlayToken.E, PlayToken.E, PlayToken.E])

    def test_markBoardOutOfBounds(self):
        self.assertFalse(self.b.mark_square(3, 3, PlayToken.X))

    def test_markBoardBadInput(self):
        self.assertFalse(self.b.mark_square(2, 2, 10))



class TestBoardHasWinner(unittest.TestCase):
    def test_hasWinner(self):
        b = Board()
        b.mark_square(0,0,PlayToken.X)
        b.mark_square(1,0,PlayToken.X)
        b.mark_square(2,0,PlayToken.X)
        self.assertTrue(b.has_winner())

    def test_noWinner(self):
        b = Board()
        self.assertFalse(b.has_winner())


class TestBoardValidInput(unittest.TestCase):
    def test_invalidInput(self):
        b = Board()
        self.assertFalse(b.valid_input(3, 3))

    def test_validInput(self):
        b = Board()
        self.assertTrue(b.valid_input(1, 1))

if __name__ == '__main__':
    print("here")
    unittest.main()
    print("here")
