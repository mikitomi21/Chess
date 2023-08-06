from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Knight(Piece, ABC):
    def __init__(self, start_position: Point, player: int):
        super().__init__(start_position, player)

    @classmethod
    def set_start_positions(cls) -> None:
        cls.board.get_square("b1").piece = Knight("b1", PLAYER_WHITE)
        cls.board.get_square("g1").piece = Knight("g1", PLAYER_WHITE)

        cls.board.get_square("b8").piece = Knight("b8", PLAYER_BLACK)
        cls.board.get_square("g8").piece = Knight("g8", PLAYER_BLACK)

    def move(self, position: Point) -> None:
        pass

    def can_move(self) -> bool:
        pass

    def __str__(self) -> str:
        return "Knight"
