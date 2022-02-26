from figure import Figure
from field_function import tuple_to_string


class Pawn(Figure):
    def __init__(self, x, y, color="white"):
        super().__init__(x, y)
        self.name = "Pawn"
        self.color = color
        # print(self.position)

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
            if new_y <= len(self.board):
                avail_moves.append(self.board[self.y + 1][self.x])
            else:
                pass

            if self.first_move():
                new_y = self.y + 2
                avail_moves.append(self.board[self.y + 2][self.x])

        else:
            new_y = self.y - 1
            if new_y >= 0:
                avail_moves.append(self.board[new_y][self.x])
            else:
                pass

            if self.first_move():
                avail_moves.append(self.board[new_y - 1][self.x])

        return tuple_to_string(avail_moves)

    def validate_move(self, x_dest, y_dest):
        return super().validate_move(x_dest, y_dest)


class Rook(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Rook"

    def list_available_moves(self):
        avail_moves = []

        for i in range(len(self.board)):
            if (
                self.board[i][self.x] != self.position
                and self.board[self.y][i] != self.position
            ):
                avail_moves.append(self.board[i][self.x])
                avail_moves.append(self.board[self.y][i])

        return tuple_to_string(avail_moves)

    def validate_move(self, x_dest, y_dest):
        return super().validate_move(x_dest, y_dest)


class Bishop(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Bishop"

    def list_available_moves(self):
        avail_moves = []
        print(len(self.board))

        def append(dx, dy):
            for i in range(len(self.board)):
                new_x = self.x + dx * i
                new_y = self.y + dy * i
                if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board):
                    if new_x != self.x and new_y != self.y:
                        if self.board[new_y][new_x] not in avail_moves:
                            avail_moves.append(self.board[new_y][new_x])
                else:
                    pass

        for dx in (-1, 1):
            for dy in (-1, 1):
                append(dx, dy)

        return tuple_to_string(avail_moves)

    def validate_move(self, x_dest, y_dest):
        return super().validate_move(x_dest, y_dest)


class Knight(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Knight"

    def list_available_moves(self):
        avail_moves = []
        knight_possible_moves = [
            (-2, -1),
            (-2, +1),
            (+2, -1),
            (+2, +1),
            (-1, -2),
            (-1, +2),
            (+1, -2),
            (+1, +2),
        ]

        for y, x in knight_possible_moves:
            new_x = self.x + x
            new_y = self.y + y

            if 0 < new_x < len(self.board) and 0 < new_y < len(self.board):
                avail_moves.append(self.board[new_y][new_x])

        return tuple_to_string(avail_moves)

    def validate_move(self, x_dest, y_dest):
        return super().validate_move(x_dest, y_dest)


class Queen(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Queen"

    def list_available_moves(self):
        avail_moves = []

        for i in range(len(self.board)):
            if (
                self.board[i][self.x] != self.position
                and self.board[self.y][i] != self.position
            ):
                avail_moves.append(self.board[i][self.x])
                avail_moves.append(self.board[self.y][i])

        def append(dx, dy):
            for i in range(len(self.board)):
                new_x = self.x + dx * i
                new_y = self.y + dy * i
                if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board):
                    if new_x != self.x and new_y != self.y:
                        if self.board[new_y][new_x] not in avail_moves:
                            avail_moves.append(self.board[new_y][new_x])
                else:
                    pass

        for dx in (-1, 1):
            for dy in (-1, 1):
                append(dx, dy)

        return tuple_to_string(avail_moves)

        return tuple_to_string(avail_moves)

    def validate_move(self, x_dest, y_dest):
        return super().validate_move(x_dest, y_dest)


class King(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "King"

    def list_available_moves(self):
        avail_moves = []

        king_possible_moves = [
            (0, +1),
            (+1, 0),
            (+1, +1),
            (0, -1),
            (-1, 0),
            (-1, -1),
            (-1, 1),
            (1, -1),
        ]
        for y, x in king_possible_moves:
            new_x = self.x + x
            new_y = self.y + y

            if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board):
                avail_moves.append(self.board[new_y][new_x])

        return tuple_to_string(avail_moves)

    def validate_move(self, x_dest, y_dest):
        return super().validate_move(x_dest, y_dest)
