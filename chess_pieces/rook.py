from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Rook(Piece, ABC):
    def __init__(self, position: str, player: int):
        super().__init__(position, player)

    @classmethod
    def set_start_positions(cls) -> None:
        cls.board.get_square("a1").piece = Rook("a1", PLAYER_WHITE)
        cls.board.get_square("a1").set_image_path("img/white/rook.png")
        cls.board.get_square("h1").piece = Rook("h1", PLAYER_WHITE)
        cls.board.get_square("h1").set_image_path("img/white/rook.png")

        cls.board.get_square("a8").piece = Rook("a8", PLAYER_BLACK)
        cls.board.get_square("a8").set_image_path("img/black/rook.png")
        cls.board.get_square("h8").piece = Rook("h8", PLAYER_BLACK)
        cls.board.get_square("h8").set_image_path("img/black/rook.png")

    def move(self, position: str) -> None:
        pass

    def can_move(self) -> bool:
        pass

    def __str__(self) -> str:
        return "Rook"
