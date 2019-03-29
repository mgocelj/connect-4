class Wins():
    """Checks after each move to see if there has been a winning move"""

    def __init__(self):
        self.diagoncounter = 0

    def check_horizontal(self, board):
        for row in board:
            redcounter = 0
            blackcounter = 0
            winner = '0'
            for piece in row:
                if piece == 'R':
                    redcounter += 1
                    blackcounter = 0
                if piece == 'B':
                    blackcounter += 1
                    redcounter = 0
                if piece == '0':
                    blackcounter = 0
                    redcounter = 0
                if redcounter == 4:
                    winner = 'R'
                    break
                if blackcounter == 4:
                    winner = 'B'
                    break
            if winner != '0':
                break
        return winner

    def reconstruct_vertical(self, board):
        counter = 0
        newboard = []
        while counter < 7:
            newrow = []
            for row in board:
                newrow.append(row[counter])
            newboard.append(newrow)
            counter += 1
        return newboard

    def check_vertical(self, board):
        newboard = self.reconstruct_vertical(board)
        for row in newboard:
            redcounter = 0
            blackcounter = 0
            winner = '0'
            for piece in row:
                if piece == 'R':
                    redcounter += 1
                    blackcounter = 0
                if piece == 'B':
                    blackcounter += 1
                    redcounter = 0
                if piece == '0':
                    blackcounter = 0
                    redcounter = 0
                if redcounter == 4:
                    winner = 'R'
                    break
                if blackcounter == 4:
                    winner = 'B'
                    break
            if winner != '0':
                break
        return winner

    def check_diagonal(self, position, board, player):
            self.check_upleft(position, board, player)
            self.check_downright(position, board, player)
            if self.diagoncounter >= 3:
                return player
            else:
                self.diagoncounter = 0
            self.check_upright(position, board, player)
            self.check_downleft(position, board, player)
            if self.diagoncounter >= 3:
                return player
            else:
                self.diagoncounter = 0
                return '0'

    def check_upleft(self, position, board, player):
        try:
            if board[position[0] - 1][position[1] -1]:
                newpos = [board[position[0] - 1][position[1] - 1]]
                if newpos[0] == player:
                    self.diagoncounter += 1
                    nextcheck = [position[0] -1, position[1] - 1]
                    self.check_upleft(nextcheck, board, player)
        except IndexError:
            return

    def check_downright(self, position, board, player):
        try:
            if board[position[0] + 1][position[1] + 1]:
                newpos = [board[position[0] + 1][position[1] + 1]]
                if newpos[0] == player:
                    self.diagoncounter += 1
                    nextcheck = [position[0] + 1, position[1] + 1]
                    self.check_downright(nextcheck, board, player)
        except IndexError:
            return

    def check_upright(self, position, board, player):
        try:
            if board[position[0] - 1][position[1] + 1]:
                newpos = [board[position[0] - 1][position[1] + 1]]
                if newpos[0] == player:
                    self.diagoncounter += 1
                    nextcheck = [position[0] - 1, position[1] + 1]
                    self.check_upright(nextcheck, board, player)
        except IndexError:
            return

    def check_downleft(self, position, board, player):
        try:
            if board[position[0] + 1][position[1] - 1]:
                newpos = [board[position[0] + 1][position[1] - 1]]
                if newpos[0] == player:
                    self.diagoncounter += 1
                    nextcheck = [position[0] + 1, position[1] - 1]
                    self.check_downleft(nextcheck, board, player)
        except IndexError:
            return

    def check_win(self, position, board, player):
        if self.check_horizontal(board) != '0':
            return self.check_horizontal(board)
        if self.check_vertical(board) != '0':
            return self.check_vertical(board)
        if self.check_diagonal(board=board, position=position, player=player)\
                != '0':
            return self.check_diagonal(board=board, position=position, player=player)
        else:
            return '0'