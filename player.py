from PlayToken import PlayToken

class Player:
    def __init__(self, tokenType : PlayToken):
        self.tokenType = tokenType

if __name__ == '__main__':
    play = Player(PlayToken.X)