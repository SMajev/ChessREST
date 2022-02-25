from figures import *


class API:
    def show_avail_moves_request(self, figure, x, y):
        if figure == "pawn":
            pawn = Pawn(x, y)
            return pawn.list_available_moves()

        if figure == "rook":
            rook = Rook(x, y)
            return rook.list_available_moves()

        if figure == "bishop":
            bishop = Bishop(x, y)
            return bishop.list_available_moves()

        if figure == "knight":
            knight = Knight(x, y)
            return knight.list_available_moves()

        if figure == "queen":
            queen = Queen(x, y)
            return queen.list_available_moves()

        if figure == "king":
            king = King(x, y)
            return king.list_available_moves()

        else:
            return False

    def validate_move(self, figure, x, y, x_dest, y_dest):
        if figure == "pawn":
            pawn = Pawn(x, y)
            return pawn.validate_move(x_dest, y_dest)

        if figure == "rook":
            rook = Rook(x, y)
            return rook.validate_move(x_dest, y_dest)

        if figure == "bishop":
            bishop = Bishop(x, y)
            return bishop.validate_move(x_dest, y_dest)

        if figure == "knight":
            knight = Knight(x, y)
            return knight.validate_move(x_dest, y_dest)

        if figure == "queen":
            queen = Queen(x, y)
            return queen.validate_move(x_dest, y_dest)

        if figure == "king":
            king = King(x, y)
            return king.validate_move(x_dest, y_dest)

        else:
            return False
