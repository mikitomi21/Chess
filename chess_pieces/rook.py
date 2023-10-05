from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Rook(Piece, ABC):
    def __init__(self, position: str, player: int, board, notation_table):
        super().__init__(position, player, board, notation_table)
        self.moved = False

    @classmethod
    def set_start_positions(cls, board, notation_table) -> None:
        board.get_square("a1").piece = Rook("a1", PLAYER_WHITE, board, notation_table)
        board.get_square("a1").set_image_path("img/white/rook.png")
        board.get_square("h1").piece = Rook("h1", PLAYER_WHITE, board, notation_table)
        board.get_square("h1").set_image_path("img/white/rook.png")

        board.get_square("a8").piece = Rook("a8", PLAYER_BLACK, board, notation_table)
        board.get_square("a8").set_image_path("img/black/rook.png")
        board.get_square("h8").piece = Rook("h8", PLAYER_BLACK, board, notation_table)
        board.get_square("h8").set_image_path("img/black/rook.png")

    def get_all_possible_moves(self) -> list[str]:
        possible_moves = []
        y, x = Point.get_position(self.position)

        if x < SIZE_OF_BOARD - 1:
            for i in range(x + 1, SIZE_OF_BOARD):
                if (
                    self.board.get_square_ints(y, i).piece
                    and self.board.get_square_ints(y, i).piece.player != self.player
                ):
                    possible_moves.append(Point.get_position_int(y, i))
                    break
                if self.board.get_square_ints(y, i).piece is not None:
                    break
                possible_moves.append(Point.get_position_int(y, i))

        if x > 0:
            for i in range(x - 1, -1, -1):
                if (
                    self.board.get_square_ints(y, i).piece
                    and self.board.get_square_ints(y, i).piece.player != self.player
                ):
                    possible_moves.append(Point.get_position_int(y, i))
                    break
                if self.board.get_square_ints(y, i).piece is not None:
                    break
                possible_moves.append(Point.get_position_int(y, i))

        if y < SIZE_OF_BOARD - 1:
            for i in range(y + 1, SIZE_OF_BOARD):
                if (
                    self.board.get_square_ints(i, x).piece
                    and self.board.get_square_ints(i, x).piece.player != self.player
                ):
                    possible_moves.append(Point.get_position_int(i, x))
                    break
                if self.board.get_square_ints(i, x).piece is not None:
                    break
                possible_moves.append(Point.get_position_int(i, x))

        if y > 0:
            for i in range(y - 1, -1, -1):
                if (
                    self.board.get_square_ints(i, x).piece
                    and self.board.get_square_ints(i, x).piece.player != self.player
                ):
                    possible_moves.append(Point.get_position_int(i, x))
                    break
                if self.board.get_square_ints(i, x).piece is not None:
                    break
                possible_moves.append(Point.get_position_int(i, x))

        return possible_moves

    def move(self, position: str) -> None:
        super().move(position)
        self.moved = True

    def get_notation_move(self, pos: str) -> str:
        notation = "R"
        if self.board.get_square(pos).piece:
            notation += "x"
        notation += pos

        return notation

    def __str__(self) -> str:
        return "Rook"
