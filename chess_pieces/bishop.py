from abc import ABC

from piece import Piece
from point import Point


class Bishop(Piece, ABC):
    def __init__(self, start_position: Point, player: int):
        super().__init__(start_position, player)

    def set_start_positions(self, color: str) -> None:
        pass

    def move(self, position: Point) -> None:
        pass

    def can_move(self) -> bool:
        pass
