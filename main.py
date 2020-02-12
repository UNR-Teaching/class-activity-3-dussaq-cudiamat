from board_controller import Board_controller
from tictactoe import Board
from modelView import ModelView

game = Board_controller(Board())
game.start_game()
#board.play_game()

#if __name__ == '__main__':
#    board = Board()
    #winner = board.play_game()
    #print("{} has won!".format(winner))
