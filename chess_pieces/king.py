from abc import ABC

from chess_pieces.piece import Piece
from chess_pieces.rook import Rook
from point import Point

from constants import *


class Castling_Options:
    def __init__(self):
        self.can_castling: bool = False
        self.options: str = []

    def add_option(self, option: str) -> None:
        self.can_castling = True
        self.options.append(option)

    def get_can_castling(self) -> bool:
        return self.can_castling

    def get_options(self) -> list[str]:
        return self.options


class King(Piece, ABC):
    def __init__(self, position: str, player: int, board, notation_table):
        super().__init__(position, player, board, notation_table)
        self.moved = False
        self.castling_check = Castling_Options()
        self.check = False

    @classmethod
    def set_start_positions(cls, board, notation_table) -> None:
        board.get_square("e1").piece = King("e1", PLAYER_WHITE, board, notation_table)
        board.get_square("e1").set_image_path("img/white/king.png")

        board.get_square("e8").piece = King("e8", PLAYER_BLACK, board, notation_table)
        board.get_square("e8").set_image_path("img/black/king.png")

    def get_all_possible_moves(self) -> list[str]:
        possible_moves = []
        y, x = Point.get_position(self.position)

        x_pos = [1, 1, 1, 0, -1, -1, -1, 0]
        y_pos = x_pos[len(x_pos) - 2 :] + x_pos[: len(x_pos) - 2]

        for i in range(len(x_pos)):
            if (
                y + y_pos[i] < SIZE_OF_BOARD
                and y + y_pos[i] >= 0
                and x + x_pos[i] < SIZE_OF_BOARD
                and x + x_pos[i] >= 0
                and (
                    self.board.get_square_ints(y + y_pos[i], x + x_pos[i]).piece is None
                    or self.board.get_square_ints(
                        y + y_pos[i], x + x_pos[i]
                    ).piece.player
                    != self.player
                )
            ):
                possible_moves.append(
                    Point.get_position_int(y + y_pos[i], x + x_pos[i])
                )

        if not self.moved:
            x_dir, x_rook = [-1, 1], [0, 7]
            for i in range(len(x_dir)):
                can_add = True
                for j in range(x + x_dir[i], x_rook[i], x_dir[i]):
                    if self.board.get_square_ints(y, j).piece is not None:
                        can_add = False
                        break
                piece = self.board.get_square_ints(y, x_rook[i]).piece
                if (
                    can_add
                    and piece
                    and isinstance(piece, Rook)
                    and piece.player == self.player
                    and not piece.moved
                ):
                    possible_moves.append(piece.position)
                    self.castling_check.add_option(piece.position)
        # print(possible_moves)
        return possible_moves

    def castling(self, pos: str) -> None:
        piece = self.board.get_square(pos).piece
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
        self.castling_check = None

    def move(self, position: str) -> None:
        if (
            not self.moved
            and self.castling_check.get_can_castling()
            and position in self.castling_check.get_options()
        ):
            self.castling(position)
        else:
            super().move(position)

        self.moved = True

    def can_move(self, pos: str) -> bool:
        if pos in self.get_all_possible_moves():
            return True
        return False

    def get_notation_move(self, pos: str):
        if not self.moved and isinstance(self.board.get_square(pos).piece, Rook):
            return "O-O-O" if pos[0] == "a" else "O-O"

        notation = "K"
        if self.board.get_square(pos).piece:
            notation += "x"
        notation += pos

        return notation

    def __str__(self) -> str:
        return "King"
