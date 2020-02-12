from playToken import PlayToken

class Board:

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.tictactoeBoard = []
        # 0-8
        # 0 - empty space, 1 - x's, 2 - o's
        for x in range(9):
            self.tictactoeBoard.append(PlayToken.E)

    def valid_input(self, column,row):
        input = (row*3) + column
        if(input >= 0 and input <= 8):
            return True
        else:
            return False

    def mark_square(self, column:int, row:int, token:PlayToken):
        """
        Marks a square at coordinate (column, row) 

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (PlayToken) the X or O representation of which player to mark in square

        :return: ????
        """
        # Bounds checking for playtoken
        if (token != PlayToken.X) or (token != PlayToken.O):
            return False

        # Check if the column and the row is valid input, if it is then mark the square
        # Also check if the space is already taken
        if(self.valid_input(column,row)):
            input = (row*3) + column

            # Check if space is taken
            if(self.tictactoeBoard[input] != PlayToken.E):
                return False
            
            self.tictactoeBoard[input] = token
            return True
        else:
            return False

    # Check if board is in win state
    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """
        
        # Check Columns 0-2
        for columns in range(2):
            print("columns: " + str(columns))
            if(self.tictactoeBoard[columns] == self.tictactoeBoard[columns+3] and
               self.tictactoeBoard[columns+3] == self.tictactoeBoard[columns+6] and
               (self.tictactoeBoard[columns] == PlayToken.X or
                self.tictactoeBoard[columns] == PlayToken.O)):
                return True

        # Check Rows..        
        for rows in range(0,7,3): # rows should equal 0, 3, 6
            if(self.tictactoeBoard[rows] == self.tictactoeBoard[rows+1] and
               self.tictactoeBoard[rows+1] == self.tictactoeBoard[rows+2] and
               (self.tictactoeBoard[rows] == PlayToken.X or
                self.tictactoeBoard[rows] == PlayToken.O)):
                return True

        # Check Diagonals
        if(self.tictactoeBoard[0] == self.tictactoeBoard[4] and
           self.tictactoeBoard[4] == self.tictactoeBoard[8] and
               (self.tictactoeBoard[0] == PlayToken.X or
                self.tictactoeBoard[0] == PlayToken.O)):
            return True
        if(self.tictactoeBoard[2] == self.tictactoeBoard[4] and
           self.tictactoeBoard[4] == self.tictactoeBoard[6] and
               (self.tictactoeBoard[2] == PlayToken.X or
                self.tictactoeBoard[2] == PlayToken.O)):
            return True

        # Failed All Checks for winners
        return False
        

    def get_board(self):
        return self.tictactoeBoard

    '''
    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        
        while(not self.has_winner()):
            # Input from player
            print("Type in position (column, row, symbol)")
            c = input()
            r = input()
            s = input()

            # Mark Square Attempt
            if(not self.mark_square(int(c),int(r), s)):
                print("Square mark Failed. Input again")
            else:
                print("Square Marked")

            

    def display_board(self):
 
for i in range(2):
            for x in range(2):
                print(self.tictactoeBoard[(x*3)+i])
            print()

       for i in range(len(self.tictactoeBoard)):
           print(i)
           print(self.tictactoeBoard[i])
       '''
            
        

