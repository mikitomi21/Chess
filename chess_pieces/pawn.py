from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Pawn(Piece, ABC):
    def __init__(self, position: str, player: int, board):
        super().__init__(position, player, board)
        self.moved = False

    @classmethod
    def set_start_positions(cls, board) -> None:
        for i in range(NUMBER_OF_PAWNS):
            pos_white = chr(i + 97) + "2"
            pos_black = chr(i + 97) + "7"
            board.get_square(pos_white).piece = Pawn(pos_white, PLAYER_WHITE, board)
            board.get_square(pos_white).set_image_path("img/white/pawn.png")

            board.get_square(pos_black).piece = Pawn(pos_black, PLAYER_BLACK, board)
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

        # print(possible_moves)

        return possible_moves

    def move(self, position: str) -> None:
        super().move(position)
        self.moved = True

    def __str__(self) -> str:
        return "pawn"
