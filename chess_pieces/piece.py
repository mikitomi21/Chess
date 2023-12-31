import copy
from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def __init__(self, position: str, player: int, board, notation_table):
        self.position = position
        self.player = player
        self.board = board
        self.notation_table = notation_table

    def remove_mating_moves(self, all_possible_moves):
        from game_manager import GameManager

        available_moves = []
        for move in all_possible_moves:
            if GameManager.simulate_move(self.position, move):
                available_moves.append(move)
        return available_moves

    @abstractmethod
    def get_all_possible_moves(self) -> list[str]:
        pass

    def get_position(self) -> str:
        return self.position

    def move(self, position: str) -> None:
        image_path = self.board.get_square(self.position).get_image_path()
        self.board.get_square(self.position).set_image_path(None)
        self.board.get_square(self.position).piece = None

        self.board.get_square(position).piece = self
        self.board.get_square(position).set_image_path(image_path)
        self.position = position

    def can_move(self, pos: str) -> bool:
        from game_manager import GameManager

        return pos in self.get_all_possible_moves() and GameManager.simulate_move(
            self.position, pos
        )

    @abstractmethod
    def get_notation_move(self, pos: str) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def __deepcopy__(self, memo):
        new_piece = self.__class__(
            self.position, self.board, self.player, self.notation_table
        )
        new_piece.position = self.position
        new_piece.board = copy.deepcopy(self.board, memo)
        new_piece.player = self.player
        return new_piece
