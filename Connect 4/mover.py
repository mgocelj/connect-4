from board import Board#

class Mover():
    """Contains methods which change important game states - the state of the
    board, the current player, and the most recently made move"""
    def __init__(self):
        self.board = Board()
        self.player = 'R'
        self.moveinfo = []

    def make_move(self, move):
        self.change_board(move, self.player)

    def change_board(self, move, player):
        current = 0
        move -= 1
        if self.board.board[current][move]!= '0':
            print("Error! This column is full. Please make a new move.")
            newmove = input("Please input your new move.")
            self.make_move(int(newmove))
            return
        while True:
            next = current + 1
            self.board.board[current][move] = player
            if next < 6 and self.board.board[next][move] == '0':
                self.board.board[current][move] = '0'
                current += 1
                continue
            else:
                break
        self.store_move(column=current, row=move)

    def change_player(self):
        if self.player == 'R':
            self.player = 'B'
        elif self.player == 'B':
            self.player = 'R'

    def store_move(self, column, row):
        self.moveinfo = [column, row]

#test = Mover()

