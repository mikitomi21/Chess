from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class King(Piece, ABC):
    def __init__(self, position: str, player: int, board):
        super().__init__(position, player, board)

    @classmethod
    def set_start_positions(cls, board) -> None:
        board.get_square("e1").piece = King("e1", PLAYER_WHITE, board)
        board.get_square("e1").set_image_path("img/white/king.png")

        board.get_square("e8").piece = King("e8", PLAYER_BLACK, board)
        board.get_square("e8").set_image_path("img/black/king.png")

    def can_move(self, pos: str) -> bool:
        # TODO add checks
        y, x = Point.get_position(self.position)
        y_new, x_new = Point.get_position(pos)
        if (
            (
                self.board.get_square(pos).piece is None
                or self.board.get_square(pos).piece.player != self.player
            )
            and abs(x - x_new) <= 1
            and abs(y - y_new) <= 1
        ):
            return True
        return False

    def __str__(self) -> str:
        return "King"
