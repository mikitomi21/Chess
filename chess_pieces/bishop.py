from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Bishop(Piece, ABC):
    def __init__(self, position: str, player: int, board):
        super().__init__(position, player, board)

    @classmethod
    def set_start_positions(cls, board) -> None:
        board.get_square("c1").piece = Bishop("c1", PLAYER_WHITE, board)
        board.get_square("c1").set_image_path("img/white/bishop.png")
        board.get_square("f1").piece = Bishop("f1", PLAYER_WHITE, board)
        board.get_square("f1").set_image_path("img/white/bishop.png")

        board.get_square("c8").piece = Bishop("a8", PLAYER_BLACK, board)
        board.get_square("c8").set_image_path("img/black/bishop.png")
        board.get_square("f8").piece = Bishop("f8", PLAYER_BLACK, board)
        board.get_square("f8").set_image_path("img/black/bishop.png")

    def can_move(self, pos: str) -> bool:
        y, x = Point.get_position(self.position)
        y_new, x_new = Point.get_position(pos)

        if abs(x - x_new) == abs(y - y_new) and x != x_new:
            x_dir = 1 if x_new > x else -1
            y_dir = 1 if y_new > y else -1
            for i in range(1, abs(x - x_new)):
                if (
                    self.board.get_square_ints(y + i * y_dir, x + i * x_dir).piece
                    is not None
                ):
                    return False
            if (
                self.board.get_square_ints(y_new, x_new).piece
                and self.board.get_square_ints(y_new, x_new).piece.player == self.player
            ):
                return False
            return True
        return False

    def __str__(self) -> str:
        return "Bishop"
