from abc import ABC, abstractmethod

class Piece(ABC):

    @abstractmethod
    def __init__(self, position: str, player: int, board):
        self.position = position
        self.player = player
        self.board = board

    @abstractmethod
    def move(self, position: str) -> None:
        pass

    @abstractmethod
    def can_move(self, position: str) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
