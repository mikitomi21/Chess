from abc import ABC

from chess_pieces.piece import Piece
from chess_pieces.rook import Rook
from point import Point

from constants import *


class King(Piece, ABC):
    def __init__(self, position: str, player: int, board):
        super().__init__(position, player, board)
        self.moved = False
        self.castling_check = (False, None)

    @classmethod
    def set_start_positions(cls, board) -> None:
        board.get_square("e1").piece = King("e1", PLAYER_WHITE, board)
        board.get_square("e1").set_image_path("img/white/king.png")

        board.get_square("e8").piece = King("e8", PLAYER_BLACK, board)
        board.get_square("e8").set_image_path("img/black/king.png")

    def get_all_possible_moves(self) -> list[str]:
        pass

    def castling(self) -> None:
        piece = self.castling_check[1]
        y_king, x_king = Point.get_position(self.position)
        y, x = Point.get_position(piece.position)

        image_king = self.board.get_square(self.position).get_image_path()
        image_rook = self.board.get_square(piece.position).get_image_path()

        self.board.get_square(self.position).set_image_path(None)
        self.board.get_square(self.position).piece = None

        self.board.get_square(piece.position).set_image_path(None)
        self.board.get_square(piece.position).piece = None

        x_dir = 1 if x_king < x else -1
        self.board.get_square_ints(y_king, x_king + (2 * x_dir)).piece = self
        self.board.get_square_ints(y_king, x_king + (2 * x_dir)).set_image_path(
            image_king
        )
        self.position = Point.get_position_int(y_king, x_king + (2 * x_dir))

        self.board.get_square_ints(y_king, x_king + (1 * x_dir)).piece = piece
        self.board.get_square_ints(y_king, x_king + (1 * x_dir)).set_image_path(
            image_rook
        )
        piece.position = Point.get_position_int(y_king, x_king + (1 * x_dir))

        piece.moved = True
        self.castling_check = (False, None)

    def move(self, pos: str) -> None:
        if self.castling_check[0]:
            self.castling()
        else:
            image_path = self.board.get_square(self.position).get_image_path()
            self.board.get_square(self.position).set_image_path(None)
            self.board.get_square(self.position).piece = None

            self.board.get_square(pos).piece = self
            self.board.get_square(pos).set_image_path(image_path)
            self.position = pos

        self.moved = True

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
        if not self.moved and y_new == y and x_new in (0, 7):
            x_dir = 1 if x_new > x else -1
            for i in range(x + x_dir, x_new, x_dir):
                if self.board.get_square_ints(y, i).piece is not None:
                    return False
            piece = self.board.get_square_ints(y_new, x_new).piece
            if (
                piece
                and isinstance(piece, Rook)
                and piece.player == self.player
                and not piece.moved
            ):
                self.castling_check = (True, piece)
                return True

        return False

    def __str__(self) -> str:
        return "King"
