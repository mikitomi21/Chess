from constants import *
from board import Board, Square

from chess_pieces.piece import Piece
from chess_pieces.bishop import Bishop
from chess_pieces.king import King
from chess_pieces.knight import Knight
from chess_pieces.pawn import Pawn
from chess_pieces.queen import Queen
from chess_pieces.rook import Rook


class Game_Manager:
    current_player = PLAYER_WHITE
    selected_piece: Piece = None
    selected_square: Square = None
    board: Board = None

    @classmethod
    def create_board(cls, root) -> None:
        cls.board = Board(root)

    @classmethod
    def set_board(cls, board: Board) -> None:
        cls.board = board

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
    def get_selected_piece(cls) -> Piece:
        return cls.selected_piece

    @classmethod
    def set_selected_piece(cls, piece) -> None:
        cls.selected_piece = piece

    @classmethod
    def get_selected_square(cls) -> Square:
        return cls.selected_square

    @classmethod
    def set_selected_square(cls, square) -> None:
        cls.selected_square = square

    @classmethod
    def try_move_piece(cls, square) -> None:
        pos: str = chr(97 + square.row) + str(8 - square.col)
        if cls.selected_piece.can_move(pos):
            cls.selected_piece.move(pos)
            cls.board.draw_pieces([square, cls.selected_square])
            cls.set_selected_piece(None)
            cls.next_player()

        else:
            cls.set_selected_piece(square.piece)
            cls.set_selected_square(square)

        if square.piece:
            print(
                f"{pos}: {square.piece} {'Black' if square.piece.player else 'White'}"
            )
        else:
            print(f"{pos}")

    @classmethod
    def set_start_positions(cls) -> None:
        Bishop.set_start_positions(cls.board)
        King.set_start_positions(cls.board)
        Knight.set_start_positions(cls.board)
        Pawn.set_start_positions(cls.board)
        Queen.set_start_positions(cls.board)
        Rook.set_start_positions(cls.board)
