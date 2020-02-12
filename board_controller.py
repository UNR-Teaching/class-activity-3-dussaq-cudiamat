from tictactoe import Board
from playToken import PlayToken


class Board_controller:
    def __init__(self, b:Board):
        self.board = b
        self.currentToken = PlayToken.X

    def mark_square(self, column:int, row:int, token:PlayToken):
        return self.board.mark_square(column, row, token)

    def check_win(self):
        if self.board.has_winner():
            return True
        else:
            return False

    def get_move(self):
        x, y = [int(x) for x in input("Enter two value: ").split()]
        return [x, y]

    def handle_turn(self):
            x, y = self.get_move()
            if self.mark_square(y, x, self.currentToken):
                if self.currentToken == PlayToken.X:
                    self.currentToken = PlayToken.O
                else:
                    self.currentToken = PlayToken.X

    def start_game(self):
        while self.check_win():
            self.handle_turn()
