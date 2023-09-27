from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class King(Piece, ABC):
    def __init__(self, position: str, player: int, board):
        super().__init__(position, player, board)

    @classmethod
    def set_start_positions(cls, board) -> None:
        board.get_square("e1").piece = King("e1", PLAYER_WHITE, board)
        board.get_square("e1").set_image_path("img/white/king.png")

        board.get_square("e8").piece = King("e8", PLAYER_BLACK, board)
        board.get_square("e8").set_image_path("img/black/king.png")

    def move(self, position: str) -> None:
        pass

    def can_move(self) -> bool:
        pass

    def __str__(self) -> str:
        return "King"
