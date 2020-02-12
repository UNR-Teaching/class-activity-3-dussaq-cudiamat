from tictactoe import Board
from board_controller import Board_controller
from modelView import ModelView
from playToken import PlayToken

import unittest

class IntegrationTests(unittest.TestCase):

    # Test if mark square in controller changes board
    def test_markControllerMarkBoard(self):
        b = Board()
        c = Board_controller(b)
        self.assertTrue(c.mark_square(0,0, PlayToken.O))

    # Test if win from board registers to controller
    def test_winSuccessfullyPassedFromBoardModel(self):
        b = Board()
        c = Board_controller(b)
        c.mark_square(0,0, PlayToken.O)
        c.mark_square(1,0, PlayToken.O)
        c.mark_square(2,0, PlayToken.O)
        self.assertTrue(c.check_win())

        
    
        
    
