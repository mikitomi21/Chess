from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Queen(Piece, ABC):
    def __init__(self, position: str, player: int, board, notation_table):
        super().__init__(position, player, board, notation_table)

    @classmethod
    def set_start_positions(cls, board, notation_table) -> None:
        board.get_square("d1").piece = Queen("d1", PLAYER_WHITE, board, notation_table)
        board.get_square("d1").set_image_path("img/white/queen.png")

        board.get_square("d8").piece = Queen("d8", PLAYER_BLACK, board, notation_table)
        board.get_square("d8").set_image_path("img/black/queen.png")

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
        notation = "Q"
        if self.board.get_square(pos).piece:
            notation += "x"
        notation += pos

        return notation

    def __str__(self) -> str:
        return "Queen"
