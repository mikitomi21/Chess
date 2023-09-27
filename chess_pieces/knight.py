from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Knight(Piece, ABC):
    def __init__(self, position: str, player: int, board):
        super().__init__(position, player, board)

    @classmethod
    def set_start_positions(cls, board) -> None:
        board.get_square("b1").piece = Knight("b1", PLAYER_WHITE, board)
        board.get_square("b1").set_image_path("img/white/knight.png")
        board.get_square("g1").piece = Knight("g1", PLAYER_WHITE, board)
        board.get_square("g1").set_image_path("img/white/knight.png")

        board.get_square("b8").piece = Knight("b8", PLAYER_BLACK, board)
        board.get_square("b8").set_image_path("img/black/knight.png")
        board.get_square("g8").piece = Knight("g8", PLAYER_BLACK, board)
        board.get_square("g8").set_image_path("img/black/knight.png")

    def get_all_possible_moves(self) -> list[str]:
        possible_moves = []
        y, x = Point.get_position(self.position)

        x_pos = [1, 2, 2, 1, -1, -2, -2, -1]
        y_pos = x_pos[2:] + x_pos[:2]

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

        return possible_moves

    def __str__(self) -> str:
        return "Knight"
