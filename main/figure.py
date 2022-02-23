from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def list_available_moves(self):
        pass

    @abstractmethod
    def validate_move(self, dest_field):
        pass
