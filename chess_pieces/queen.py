from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Queen(Piece, ABC):
    def __init__(self, start_position: Point, player: int):
        super().__init__(start_position, player)

    @classmethod
    def set_start_positions(cls) -> None:
        cls.board.get_square("d1").piece = Queen("d1", PLAYER_WHITE)

        cls.board.get_square("d8").piece = Queen("d8", PLAYER_BLACK)

    def move(self, position: Point) -> None:
        pass

    def can_move(self) -> bool:
        pass

    def __str__(self) -> str:
        return "Queen"
