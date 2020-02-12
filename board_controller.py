from tictactoe import Board
from playToken import PlayToken


class Board_controller:
    def __init__(self, b:Board):
        self.board = b

    def mark_square(self, column:int, row:int, token:PlayToken):
        self.board.mark_square(column, row, token)

    def check_win(self):
        if self.board.has_winner():
            return True
        else:
            return False

        
