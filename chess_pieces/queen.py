from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Queen(Piece, ABC):
    def __init__(self, position: str, player: int, board):
        super().__init__(position, player, board)

    @classmethod
    def set_start_positions(cls, board) -> None:
        board.get_square("d1").piece = Queen("d1", PLAYER_WHITE, board)
        board.get_square("d1").set_image_path("img/white/queen.png")

        board.get_square("d8").piece = Queen("d8", PLAYER_BLACK, board)
        board.get_square("d8").set_image_path("img/black/queen.png")

    def can_move(self, pos: str) -> bool:
        y, x = Point.get_position(self.position)
        y_new, x_new = Point.get_position(pos)

        if x == x_new:
            for i in range(min(y, y_new) + 1, max(y, y_new)):
                if self.board.get_square_ints(i, x).piece is not None:
                    return False
            if (
                self.board.get_square_ints(y_new, x).piece
                and self.board.get_square_ints(y_new, x).piece.player == self.player
            ):
                return False
            return True
        elif y == y_new:
            for i in range(min(x, x_new) + 1, max(x, x_new)):
                if self.board.get_square_ints(y, i).piece is not None:
                    return False
            if (
                self.board.get_square_ints(y, x_new).piece
                and self.board.get_square_ints(y, x_new).piece.player == self.player
            ):
                return False
            return True
        elif abs(x - x_new) == abs(y - y_new) and x != x_new:
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
        return "Queen"
