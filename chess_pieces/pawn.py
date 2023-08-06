from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Pawn(Piece, ABC):
    def __init__(self, position: str, player: int):
        super().__init__(position, player)
        self.moved = False

    @classmethod
    def set_start_positions(cls) -> None:
        for i in range(NUMBER_OF_PAWNS):
            pos_white = chr(i + 97) + "2"
            pos_black = chr(i + 97) + "7"
            cls.board.get_square(pos_white).piece = Pawn(pos_white, PLAYER_WHITE)
            cls.board.get_square(pos_white).set_image_path("img/white/pawn.png")

            cls.board.get_square(pos_black).piece = Pawn(pos_black, PLAYER_BLACK)
            cls.board.get_square(pos_black).set_image_path("img/black/pawn.png")

    def move(self, position: str) -> None:
        self.board.get_square(self.position).piece = None
        self.board.get_square(position).piece = self
        self.moved = True

    def can_move(self, pos: str) -> bool:
        x, y = Point.get_position(self.position)
        x_new, y_new = Point.get_position(pos)

        if self.player == PLAYER_WHITE:
            if y_new - y == 1:
                return True
            elif y_new - y == 2 and not self.moved:
                return True
        elif self.player == PLAYER_BLACK:
            if y - y_new == 1:
                return True
            elif y - y_new == 2 and not self.moved:
                return True

        return False

    def __str__(self) -> str:
        return "pawn"
