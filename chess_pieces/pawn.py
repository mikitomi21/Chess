from abc import ABC

from piece import Piece
from point import Point


class Pawn(Piece, ABC):
    def __init__(self, start_position: Point, player: int):
        super().__init__(start_position, player)

    def move(self, position: Point) -> None:
        pass

    def can_move(self) -> bool:
        pass
