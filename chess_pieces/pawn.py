from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Pawn(Piece, ABC):
    def __init__(self, start_position: Point, player: int):
        super().__init__(start_position, player)

    @classmethod
    def set_start_positions(cls) -> None:
        for i in range(NUMBER_OF_PAWNS):
            cls.board.get_square(chr(i + 97) + "2").piece = Pawn(
                chr(i + 97) + "2", PLAYER_WHITE
            )
            cls.board.get_square(chr(i + 97) + "7").piece = Pawn(
                chr(i + 97) + "7", PLAYER_BLACK
            )

    def move(self, position: Point) -> None:
        pass

    def can_move(self) -> bool:
        pass

    def __str__(self) -> str:
        return "pawn"
