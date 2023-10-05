from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Pawn(Piece, ABC):
    def __init__(self, position: str, player: int, board, notation_table):
        super().__init__(position, player, board, notation_table)
        self.moved = False

    @classmethod
    def set_start_positions(cls, board, notation_table) -> None:
        for i in range(NUMBER_OF_PAWNS):
            pos_white = chr(i + 97) + "2"
            pos_black = chr(i + 97) + "7"
            board.get_square(pos_white).piece = Pawn(
                pos_white, PLAYER_WHITE, board, notation_table
            )
            board.get_square(pos_white).set_image_path("img/white/pawn.png")

            board.get_square(pos_black).piece = Pawn(
                pos_black, PLAYER_BLACK, board, notation_table
            )
            board.get_square(pos_black).set_image_path("img/black/pawn.png")

    def get_all_possible_moves(self) -> list[str]:
        possible_moves = []
        y, x = Point.get_position(self.position)

        if self.player == PLAYER_BLACK:
            if self.board.get_square_ints(y + 1, x).piece is None:
                possible_moves.append(Point.get_position_int(y + 1, x))
            if not self.moved and self.board.get_square_ints(y + 2, x).piece is None:
                possible_moves.append(Point.get_position_int(y + 2, x))
            if (
                x < SIZE_OF_BOARD - 1
                and self.board.get_square_ints(y + 1, x + 1).piece is not None
                and self.board.get_square_ints(y + 1, x + 1).piece.player
                == PLAYER_WHITE
            ):
                possible_moves.append(Point.get_position_int(y + 1, x + 1))
            if (
                x > 0
                and self.board.get_square_ints(y + 1, x - 1).piece is not None
                and self.board.get_square_ints(y + 1, x - 1).piece.player
                == PLAYER_WHITE
            ):
                possible_moves.append(Point.get_position_int(y + 1, x - 1))

        elif self.player == PLAYER_WHITE:
            if self.board.get_square_ints(y - 1, x).piece is None:
                possible_moves.append(Point.get_position_int(y - 1, x))
            if not self.moved and self.board.get_square_ints(y - 2, x).piece is None:
                possible_moves.append(Point.get_position_int(y - 2, x))
            if (
                x < SIZE_OF_BOARD - 1
                and self.board.get_square_ints(y - 1, x + 1).piece is not None
                and self.board.get_square_ints(y - 1, x + 1).piece.player
                == PLAYER_BLACK
            ):
                possible_moves.append(Point.get_position_int(y - 1, x + 1))
            if (
                x > 0
                and self.board.get_square_ints(y - 1, x - 1).piece is not None
                and self.board.get_square_ints(y - 1, x - 1).piece.player
                == PLAYER_BLACK
            ):
                possible_moves.append(Point.get_position_int(y - 1, x - 1))

        return possible_moves

    def move(self, position: str) -> None:
        super().move(position)
        # self.notation_table.save_move_to_file(self.moved)
        self.moved = True

    def get_notation_move(self, pos: str):
        notation = ""
        if self.board.get_square(pos).piece:
            notation += "x"
        notation += pos

        return notation

    def __str__(self) -> str:
        return "pawn"
