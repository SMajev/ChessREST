from figure import Figure

class Pawn(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def list_available_moves(self):
        avail_moves = self.x, self.y + 1
        print(avail_moves)

    def validate_move(self, dest_field):
        is_posible = None

class Knight(Figure):
    pass

class Bishop(Figure):
    pass

class Rook(Figure):
    pass

class Queen(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def list_available_moves(self):
        avail_moves = self.x, self.y + 1
        print(avail_moves)

    def validate_move(self, dest_field):
        is_posible = None

class King(Figure):
    pass

if __name__ == '__main__':
    pawn1 = Pawn(0,7)
    pawn1.list_available_moves()
    