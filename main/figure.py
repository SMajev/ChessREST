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
