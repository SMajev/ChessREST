from figures import *
from board import Board

class API():
    def __init__(self):
        self.board = Board().board

    def show_avail_moves_request(self, figure, x, y):
        if figure == 'pawn':
            pawn = Pawn(self.board, x, y)
            return pawn.list_available_moves()

        if figure == 'rook':
            rook = Rook(self.board, x, y)
            return rook.list_available_moves()

        if figure == 'bishop':
            bishop = Bishop(self.board, x, y)
            return bishop.list_available_moves()

        if figure == 'knight':
            knight = Knight(self.board, x, y)
            return knight.list_available_moves()

        if figure == 'queen':
            queen = Queen(self.board, x, y)
            return queen.list_available_moves()

        if figure == 'king':
            king = King(self.board, x, y)
            return king.list_available_moves()


    def validate_move(self, figure, x, y):
        if figure == 'pawn':
            pawn = Pawn(self.board, x, y)
            return pawn.validate_move(dest_field)

        if figure == 'rook':
            rook = Rook(self.board, x, y)
            return rook.validate_move(dest_field)

        if figure == 'bishop':
            bishop = Bishop(self.board, x, y)
            return bishop.validate_move(dest_field)

        if figure == 'knight':
            knight = Knight(self.board, x, y)
            return knight.validate_move(dest_field)

        if figure == 'queen':
            queen = Queen(self.board, x, y)
            return queen.validate_move(dest_field)

        if figure == 'king':
            king = King(self.board, x, y)
            return king.validate_move(dest_field)