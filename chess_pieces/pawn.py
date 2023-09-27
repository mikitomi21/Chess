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

        if self.board.get_square(pos).piece is None:
            if x == x_new:
                if self.player == PLAYER_BLACK:
                    if y_new - y == 1:
                        return True
                    elif y_new - y == 2 and not self.moved:
                        return True
                elif self.player == PLAYER_WHITE:
                    if y - y_new == 1:
                        return True
                    elif y - y_new == 2 and not self.moved:
                        return True
        else:
            if abs(x - x_new) == 1:
                if (
                    self.player == PLAYER_BLACK
                    and y_new - y == 1
                    and self.board.get_square(pos).piece.player == PLAYER_WHITE
                ):
                    return True
                elif (
                    self.player == PLAYER_WHITE
                    and y - y_new == 1
                    and self.board.get_square(pos).piece.player == PLAYER_BLACK
                ):
                    return True

        return False

    def __str__(self) -> str:
        return "pawn"
