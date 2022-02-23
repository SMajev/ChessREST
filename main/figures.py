from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def __init__(self, board, x, y):
        self.board = board
        self.name = ""
        self.color = ""
        self.y = y
        self.x = x
        self.position = self.board[self.y][self.x]

    @abstractmethod
    def list_available_moves(self):
        pass

    @abstractmethod
    def validate_move(self, dest_field):
        pass


class Pawn(Figure):
    def __init__(self, board, x, y, color="white"):
        super().__init__(board, x, y)
        self.name = "Pawn"
        self.color = color

    def first_move(self):
        if self.color == "white" and self.y == 1:
            return True
        elif self.color == "black" and self.y == 6:
            return True
        else:
            return False

    def list_available_moves(self):
        avail_moves = []
        if self.color == "white":
            new_y = self.y + 1
            new_x = self.x
            if new_y < len(self.board):
                avail_moves.append(self.board[self.y + 1][self.x])
            else: 
                pass

            if self.first_move():
                new_y = self.y + 2
                avail_moves.append(self.board[self.y + 2][self.x])

        else:
            new_y = self.y - 1
            if new_y > 0:
                avail_moves.append(self.board[new_y][self.x])
                
            else:
                pass

            if self.first_move():
                avail_moves.append(self.board[new_y - 1][self.x])


        return avail_moves

    def validate_move(self, dest_field):
        is_posible = None




class Rook(Figure):
    def __init__(self, board, x, y):
        super().__init__(board, x, y)
        self.name = 'Rook'

    def list_available_moves(self):
        avail_moves = []
        print(self.position)
        for i in range(len(self.board)):
            if self.board[i][self.x] != self.position:
                avail_moves.append(self.board[i][self.x])
        for i in range(len(self.board)):
            if self.board[self.y][i] != self.position:
                avail_moves.append(self.board[self.y][i])
        return avail_moves

    def validate_move(self, dest_field):
        is_posible = None




class Bishop(Figure):
    pass


class Knight(Figure):
    pass


class Queen(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def list_available_moves(self):
        avail_moves = []

    def validate_move(self, dest_field):
        is_posible = None


class King(Figure):
    pass


