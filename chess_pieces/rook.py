from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *

class Rook(Piece, ABC):
    def __init__(self, start_position: Point, player: int):
        super().__init__(start_position, player)

    @classmethod
    def set_start_positions(cls) -> None:
        cls.board.get_square("a1").piece = Rook("a1", PLAYER_WHITE)
        cls.board.get_square("h1").piece = Rook("h1", PLAYER_WHITE)

        cls.board.get_square("a8").piece = Rook("a8", PLAYER_BLACK)
        cls.board.get_square("h8").piece = Rook("h8", PLAYER_BLACK)

    def move(self, position: Point) -> None:
        pass

    def can_move(self) -> bool:
        pass

    def __str__(self) -> str:
        return "Rook"
