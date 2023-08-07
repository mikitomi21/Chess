from constants import *
from board import Board

from chess_pieces.piece import Piece
from chess_pieces.bishop import Bishop
from chess_pieces.king import King
from chess_pieces.knight import Knight
from chess_pieces.pawn import Pawn
from chess_pieces.queen import Queen
from chess_pieces.rook import Rook


class Game_Manager:
    current_player = PLAYER_WHITE
    chosen_piece: Piece = None
    board: Board = None

    @classmethod
    def set_board(cls, root) -> None:
        board = Board(root)
        cls.board = board.get_board()

    @classmethod
    def next_player(cls) -> None:
        if cls.current_player == PLAYER_WHITE:
            cls.current_player = PLAYER_BLACK
        else:
            cls.current_player = PLAYER_WHITE

    @classmethod
    def get_player(cls) -> int:
        return cls.current_player

    @classmethod
    def get_chosen_piece(cls) -> Piece:
        return cls.chosen_piece

    @classmethod
    def set_start_positions(cls) -> None:
        Piece.set_board(cls.board)
        Bishop.set_start_positions()
        King.set_start_positions()
        Knight.set_start_positions()
        Pawn.set_start_positions()
        Queen.set_start_positions()
        Rook.set_start_positions()

    @classmethod
    def click_piece(cls, square) -> None:
        pos: str = chr(97 + square.row) + str(8 - square.col)
        if cls.chosen_piece != None and cls.chosen_piece.can_move(pos):
            cls.chosen_piece.move(pos)
        else:
            cls.chosen_piece = square.piece

        if square.piece:
            print(
                f"{pos}: {square.piece} {'Black' if square.piece.player else 'White'}"
            )
        else:
            print(f"{pos}")
