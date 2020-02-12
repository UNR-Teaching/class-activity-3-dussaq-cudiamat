from tictactoe import Board
from modelView import ModelView

board = Board()
viewer = ModelView()
viewer.update_view(board.get_board())
#board.play_game()

#if __name__ == '__main__':
#    board = Board()
    #winner = board.play_game()
    #print("{} has won!".format(winner))
