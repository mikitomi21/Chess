from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Bishop(Piece, ABC):
    def __init__(self, position: str, player: int, board, notation_table):
        super().__init__(position, player, board, notation_table)

    @classmethod
    def set_start_positions(cls, board, notation_table) -> None:
        board.get_square("c1").piece = Bishop("c1", PLAYER_WHITE, board, notation_table)
        board.get_square("c1").set_image_path("img/white/bishop.png")
        board.get_square("f1").piece = Bishop("f1", PLAYER_WHITE, board, notation_table)
        board.get_square("f1").set_image_path("img/white/bishop.png")

        board.get_square("c8").piece = Bishop("c8", PLAYER_BLACK, board, notation_table)
        board.get_square("c8").set_image_path("img/black/bishop.png")
        board.get_square("f8").piece = Bishop("f8", PLAYER_BLACK, board, notation_table)
        board.get_square("f8").set_image_path("img/black/bishop.png")

    def get_all_possible_moves(self) -> list[str]:
        possible_moves = []
        y, x = Point.get_position(self.position)

        i = 0
        while x + i < SIZE_OF_BOARD - 1 and y + i < SIZE_OF_BOARD - 1:
            i += 1
            if (
                self.board.get_square_ints(y + i, x + i).piece
                and self.board.get_square_ints(y + i, x + i).piece.player != self.player
            ):
                possible_moves.append(Point.get_position_int(y + i, x + i))
                break
            if self.board.get_square_ints(y + i, x + i).piece is not None:
                break
            possible_moves.append(Point.get_position_int(y + i, x + i))

        i = 0
        while x + i < SIZE_OF_BOARD - 1 and y > i:
            i += 1
            if (
                self.board.get_square_ints(y - i, x + i).piece
                and self.board.get_square_ints(y - i, x + i).piece.player != self.player
            ):
                possible_moves.append(Point.get_position_int(y - i, x + i))
                break
            if self.board.get_square_ints(y - i, x + i).piece is not None:
                break
            possible_moves.append(Point.get_position_int(y - i, x + i))

        i = 0
        while x > i and y > i:
            i += 1
            if (
                self.board.get_square_ints(y - i, x - i).piece
                and self.board.get_square_ints(y - i, x - i).piece.player != self.player
            ):
                possible_moves.append(Point.get_position_int(y - i, x - i))
                break
            if self.board.get_square_ints(y - i, x - i).piece is not None:
                break
            possible_moves.append(Point.get_position_int(y - i, x - i))

        i = 0
        while x > i and y + i < SIZE_OF_BOARD - 1:
            i += 1
            if (
                self.board.get_square_ints(y + i, x - i).piece
                and self.board.get_square_ints(y + i, x - i).piece.player != self.player
            ):
                possible_moves.append(Point.get_position_int(y + i, x - i))
                break
            if self.board.get_square_ints(y + i, x - i).piece is not None:
                break
            possible_moves.append(Point.get_position_int(y + i, x - i))

        return possible_moves

    def get_notation_move(self, pos: str) -> str:
        notation = "B"
        if self.board.get_square(pos).piece:
            notation += "x"
        notation += pos

        return notation

    def __str__(self) -> str:
        return "Bishop"
