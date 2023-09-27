from abc import ABC

from chess_pieces.piece import Piece
from chess_pieces.rook import Rook
from point import Point

from constants import *


class King(Piece, ABC):
    def __init__(self, position: str, player: int, board):
        super().__init__(position, player, board)
        self.moved = False
        self.castling_check = (False, None)

    @classmethod
    def set_start_positions(cls, board) -> None:
        board.get_square("e1").piece = King("e1", PLAYER_WHITE, board)
        board.get_square("e1").set_image_path("img/white/king.png")

        board.get_square("e8").piece = King("e8", PLAYER_BLACK, board)
        board.get_square("e8").set_image_path("img/black/king.png")

    def get_all_possible_moves(self) -> list[str]:
        possible_moves = []
        y, x = Point.get_position(self.position)

        x_pos = [1,1,1,0,-1,-1,-1,0]
        y_pos = x_pos[len(x_pos)-2:] + x_pos[:len(x_pos)-2]

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

        rooks = []
        if self.player == PLAYER_WHITE:
            rooks.append(self.board.get_square_ints(7,0).piece)
            rooks.append(self.board.get_square_ints(7,7).piece)
        else:
            rooks.append(self.board.get_square_ints(0, 0).piece)
            rooks.append(self.board.get_square_ints(0, 7).piece)

        for piece in rooks:
            if (
                    piece
                    and isinstance(piece, Rook)
                    and piece.player == self.player
                    and not piece.moved
            ):
                possible_moves.append(piece.position)
        print(possible_moves)
        return possible_moves

    def castling(self) -> None:
        piece = self.castling_check[1]
        y_king, x_king = Point.get_position(self.position)
        y, x = Point.get_position(piece.position)

        image_king = self.board.get_square(self.position).get_image_path()
        image_rook = self.board.get_square(piece.position).get_image_path()

        self.board.get_square(self.position).set_image_path(None)
        self.board.get_square(self.position).piece = None

        self.board.get_square(piece.position).set_image_path(None)
        self.board.get_square(piece.position).piece = None

        x_dir = 1 if x_king < x else -1
        self.board.get_square_ints(y_king, x_king + (2 * x_dir)).piece = self
        self.board.get_square_ints(y_king, x_king + (2 * x_dir)).set_image_path(
            image_king
        )
        self.position = Point.get_position_int(y_king, x_king + (2 * x_dir))

        self.board.get_square_ints(y_king, x_king + (1 * x_dir)).piece = piece
        self.board.get_square_ints(y_king, x_king + (1 * x_dir)).set_image_path(
            image_rook
        )
        piece.position = Point.get_position_int(y_king, x_king + (1 * x_dir))

        piece.moved = True
        self.castling_check = (False, None)

    def move(self, pos: str) -> None:
        if self.castling_check[0]:
            self.castling()
        else:
            image_path = self.board.get_square(self.position).get_image_path()
            self.board.get_square(self.position).set_image_path(None)
            self.board.get_square(self.position).piece = None

            self.board.get_square(pos).piece = self
            self.board.get_square(pos).set_image_path(image_path)
            self.position = pos

        self.moved = True

    def can_move(self, pos: str) -> bool:
        if pos in self.get_all_possible_moves():
            return True
        return False

    def __str__(self) -> str:
        return "King"
