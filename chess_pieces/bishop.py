from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Bishop(Piece, ABC):
    def __init__(self, start_position: Point, player: int):
        super().__init__(start_position, player)

    @classmethod
    def set_start_positions(cls) -> None:
        cls.board.get_square("c1").piece = Bishop("a1", PLAYER_WHITE)
        cls.board.get_square("f1").piece = Bishop("f1", PLAYER_WHITE)

        cls.board.get_square("c8").piece = Bishop("a8", PLAYER_BLACK)
        cls.board.get_square("f8").piece = Bishop("f8", PLAYER_BLACK)

    def move(self, position: Point) -> None:
        pass

    def can_move(self) -> bool:
        pass

    def __str__(self) -> str:
        return "Bishop"
