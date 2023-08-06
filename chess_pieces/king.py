from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class King(Piece, ABC):
    def __init__(self, start_position: Point, player: int):
        super().__init__(start_position, player)

    @classmethod
    def set_start_positions(cls) -> None:
        cls.board.get_square("e1").piece = King("e1", PLAYER_WHITE)

        cls.board.get_square("e8").piece = King("e8", PLAYER_BLACK)

    def move(self, position: Point) -> None:
        pass

    def can_move(self) -> bool:
        pass

    def __str__(self) -> str:
        return "King"
