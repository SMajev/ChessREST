from abc import ABC, abstractmethod
from field_function import tuple_to_string
from board import Board


class Figure(ABC):
    @abstractmethod
    def __init__(self, x, y):
        self.board = Board().board
        self.name = ""
        self.color = ""
        self.y = y
        self.x = x
        self.position = self.board[self.y][self.x]
        self.moves = self.list_available_moves()

    @abstractmethod
    def list_available_moves(self):
        pass

    @abstractmethod
    def validate_move(self, x_dest, y_dest):
        dest_fields = tuple_to_string([self.board[y_dest][x_dest]])
        if dest_fields[0] in self.list_available_moves():
            return "is validate"
        else:
            return "isn't validate"

