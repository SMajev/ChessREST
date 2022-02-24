class Board:
    def __init__(self):
        self.board = []
        self._letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

        for x in range(1, 9):
            self.board.append([])

            for y in self._letters:
                self.board[x - 1].append((y, x))

    def show_board(self):
        for row in self.board:
            print(row)
