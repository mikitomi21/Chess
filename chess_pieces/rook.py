from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Rook(Piece, ABC):
    def __init__(self, position: str, player: int, board):
        super().__init__(position, player, board)
        self.moved = False

    @classmethod
    def set_start_positions(cls, board) -> None:
        board.get_square("a1").piece = Rook("a1", PLAYER_WHITE, board)
        board.get_square("a1").set_image_path("img/white/rook.png")
        board.get_square("h1").piece = Rook("h1", PLAYER_WHITE, board)
        board.get_square("h1").set_image_path("img/white/rook.png")

        board.get_square("a8").piece = Rook("a8", PLAYER_BLACK, board)
        board.get_square("a8").set_image_path("img/black/rook.png")
        board.get_square("h8").piece = Rook("h8", PLAYER_BLACK, board)
        board.get_square("h8").set_image_path("img/black/rook.png")

    def move(self, position: str) -> None:
        image_path = self.board.get_square(self.position).get_image_path()
        self.board.get_square(self.position).set_image_path(None)
        self.board.get_square(self.position).piece = None

        self.board.get_square(position).piece = self
        self.board.get_square(position).set_image_path(image_path)
        self.position = position

        self.moved = True

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

        return False

    def __str__(self) -> str:
        return "Rook"
