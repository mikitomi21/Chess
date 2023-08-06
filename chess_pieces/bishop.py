from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Bishop(Piece, ABC):
    def __init__(self, position: str, player: int):
        super().__init__(position, player)

    @classmethod
    def set_start_positions(cls) -> None:
        cls.board.get_square("c1").piece = Bishop("c1", PLAYER_WHITE)
        cls.board.get_square("c1").set_image_path("img/white/bishop.png")
        cls.board.get_square("f1").piece = Bishop("f1", PLAYER_WHITE)
        cls.board.get_square("f1").set_image_path("img/white/bishop.png")

        cls.board.get_square("c8").piece = Bishop("a8", PLAYER_BLACK)
        cls.board.get_square("c8").set_image_path("img/black/bishop.png")
        cls.board.get_square("f8").piece = Bishop("f8", PLAYER_BLACK)
        cls.board.get_square("f8").set_image_path("img/black/bishop.png")

    def move(self, position: str) -> None:
        pass

    def can_move(self) -> bool:
        pass

    def __str__(self) -> str:
        return "Bishop"
