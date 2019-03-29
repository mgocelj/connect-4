class Board():
    """Contains the board, and the method which prints the board after each turn
    """

    def __init__(self):
        self.board = [['0', '0', '0', '0', '0', '0', '0'],
                      ['0', '0', '0', '0', '0', '0', '0'],
                      ['0', '0', '0', '0', '0', '0', '0'],
                      ['0', '0', '0', '0', '0', '0', '0'],
                      ['0', '0', '0', '0', '0', '0', '0'],
                      ['0', '0', '0', '0', '0', '0', '0'],]


    def board_print(self):
        print("____________________________________")
        for row in self.board:
            print(row)
        print("____________________________________")
