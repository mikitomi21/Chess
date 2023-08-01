from abc import ABC, abstractmethod
from point import Point


class Piece(ABC):
    @abstractmethod
    def __init__(self, start_position: Point, player: int):
        self.start_position = start_position
        self.player = player

    @abstractmethod
    def move(self, position: Point) -> None:
        pass

    @abstractmethod
    def can_move(self) -> bool:
        pass
