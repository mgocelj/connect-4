from wins import Wins
from mover import Mover

class ConnectFour():
    """Contains input checker, and 'order' of functions to play the game.
    Intended to be called in Terminal"""

    def __init__(self):
        self.makemoves = Mover()
        self.checkwins = Wins()

    def check_input(self):
        while True:
            newmove = input("Please make a move. It is " + self.makemoves.player + "'s turn!")
            try:
                newmove = int(newmove)
            except:
                print("Error! Please use a numeric input.")
            else:
                if newmove > 0 and newmove < 8:
                    break
                else:
                    print("Error! Please use an input between 1 and 7.")
        return newmove

    def play_game(self):
        counter = 0
        self.makemoves.board.board_print()
        while counter < 42:
            self.makemoves.make_move(self.check_input())
            self.makemoves.board.board_print()
            wincheck = self.checkwins.check_win(position=self.makemoves.moveinfo,
                                     player=self.makemoves.player,
                                     board=self.makemoves.board.board)
            if wincheck == 'R':
                print("Game over! Red wins!")
                break
            elif wincheck == 'B':
                print("Game over! Black wins!")
                break
            else:
                self.makemoves.change_player()

newgame = ConnectFour()
newgame.play_game()