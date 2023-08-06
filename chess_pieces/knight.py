from abc import ABC

from chess_pieces.piece import Piece
from point import Point

from constants import *


class Knight(Piece, ABC):
    def __init__(self, position: str, player: int):
        super().__init__(position, player)

    @classmethod
    def set_start_positions(cls) -> None:
        cls.board.get_square("b1").piece = Knight("b1", PLAYER_WHITE)
        cls.board.get_square("b1").set_image_path("img/white/knight.png")
        cls.board.get_square("g1").piece = Knight("g1", PLAYER_WHITE)
        cls.board.get_square("g1").set_image_path("img/white/knight.png")

        cls.board.get_square("b8").piece = Knight("b8", PLAYER_BLACK)
        cls.board.get_square("b8").set_image_path("img/black/knight.png")
        cls.board.get_square("g8").piece = Knight("g8", PLAYER_BLACK)
        cls.board.get_square("g8").set_image_path("img/black/knight.png")

    def move(self, position: str) -> None:
        pass

    def can_move(self) -> bool:
        pass

    def __str__(self) -> str:
        return "Knight"
