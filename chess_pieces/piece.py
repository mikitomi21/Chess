from abc import ABC, abstractmethod
from point import Point


class Piece(ABC):
    board = None

    @abstractmethod
    def __init__(self, position: str, player: int):
        self.position = position
        self.player = player

    @abstractmethod
    def move(self, position: str) -> None:
        pass

    @abstractmethod
    def can_move(self, position: str) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @classmethod
    def set_board(cls, board) -> None:
        cls.board = board
