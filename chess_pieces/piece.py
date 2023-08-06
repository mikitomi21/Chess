from abc import ABC, abstractmethod
from point import Point
from board import Board


class Piece(ABC):
    board = None

    @abstractmethod
    def __init__(self, start_position: Point, player: int):
        self.start_position = start_position
        self.player = player

    @abstractmethod
    def set_start_positions(self, color: str) -> None:
        pass

    @abstractmethod
    def move(self, position: Point) -> None:
        pass

    @abstractmethod
    def can_move(self) -> bool:
        pass

    @classmethod
    def set_board(cls, board: Board) -> None:
        cls.board = board
