class Board:

    def __init__(self):
        self.board = []

        for x in range(9):
            self.board.append([])

            for y in range(9):
                self.board[x].append(None)
  

    def show_board(self):
        for row in self.board:
            print(row)

    def show_field(self, x, y):
        print(self.board[x][y])

    def put_figure(self, name, x, y):
        self.board[x][y] = name

if __name__ == '__main__': 
    board = Board()
    
    board.put_figure('Pionek',1, 1)
    board.show_field(1, 1)
    board.show_board()