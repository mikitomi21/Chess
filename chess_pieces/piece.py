from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def __init__(self, position: str, player: int, board):
        self.position = position
        self.player = player
        self.board = board

    def move(self, position: str) -> None:
        image_path = self.board.get_square(self.position).get_image_path()
        self.board.get_square(self.position).set_image_path(None)
        self.board.get_square(self.position).piece = None

        self.board.get_square(position).piece = self
        self.board.get_square(position).set_image_path(image_path)
        self.position = position

    @abstractmethod
    def can_move(self, position: str) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
