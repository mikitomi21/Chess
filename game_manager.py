import copy
from constants import *
from board import Board, Square
from notation_table import NotationTable

from chess_pieces.piece import Piece
from chess_pieces.bishop import Bishop
from chess_pieces.king import King
from chess_pieces.knight import Knight
from chess_pieces.pawn import Pawn
from chess_pieces.queen import Queen
from chess_pieces.rook import Rook


class GameManager:
    board: Board = None
    current_player = PLAYER_WHITE
    selected_piece: Piece = None
    selected_square: Square = None
    is_check: bool = False
    notation_table = None

    @classmethod
    def create_board(cls, root, canvas) -> None:
        cls.board = Board(root, canvas)

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
    def create_notation_table(cls, root, canvas):
        cls.notation_table = NotationTable(root, canvas)

    @classmethod
    def back_to_the_previous_setup(
        cls, board_tmp, selected_piece_tmp, is_check_tmp
    ) -> None:
        cls.board = board_tmp
        cls.selected_piece = selected_piece_tmp
        cls.is_check = is_check_tmp
        cls.board.draw_board()

    @classmethod
    def simulate_move(cls, pos_start: str, pos_end: str):
        board_tmp = cls.board
        selected_piece_tmp = cls.selected_piece
        is_check_tmp = cls.is_check

        cls.board = copy.deepcopy(cls.board)
        cls.selected_piece = cls.board.get_square(pos_start).piece
        cls.selected_piece.move(pos_end)
        cls.set_selected_piece(None)

        cls.update_check_status()
        if cls.is_check:
            cls.back_to_the_previous_setup(board_tmp, selected_piece_tmp, is_check_tmp)
            return False

        cls.back_to_the_previous_setup(board_tmp, selected_piece_tmp, is_check_tmp)
        cls.is_check = is_check_tmp
        return True

    @classmethod
    def try_move_piece(cls, square) -> None:
        pos: str = chr(97 + square.row) + str(8 - square.col)
        if cls.selected_piece.can_move(pos) and cls.simulate_move(
            cls.get_selected_piece().get_position(), pos
        ):
            notation = cls.selected_piece.get_notation_move(pos)
            cls.selected_piece.move(pos)
            cls.board.draw_pieces([square, cls.selected_square])
            cls.set_selected_piece(None)
            cls.next_player()

            cls.update_check_status()
            if cls.check_mat():
                notation += "#"
                print("Mate")
            elif cls.is_check:
                notation += "+"
                print("Check")

            cls.notation_table.save_move_to_file(notation)
            cls.notation_table.print_moves()

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
        Bishop.set_start_positions(cls.board, cls.notation_table)
        King.set_start_positions(cls.board, cls.notation_table)
        Knight.set_start_positions(cls.board, cls.notation_table)
        Pawn.set_start_positions(cls.board, cls.notation_table)
        Queen.set_start_positions(cls.board, cls.notation_table)
        Rook.set_start_positions(cls.board, cls.notation_table)

    @classmethod
    def get_player_pieces(cls, player: int) -> list[Piece]:
        pieces = []
        for y in range(SIZE_OF_BOARD):
            for x in range(SIZE_OF_BOARD):
                piece = cls.board.get_square_ints(y, x).piece
                if piece and piece.player == player:
                    pieces.append(piece)
        return pieces

    @classmethod
    def get_king(cls, player: int) -> King:
        for y in range(SIZE_OF_BOARD):
            for x in range(SIZE_OF_BOARD):
                piece = cls.board.get_square_ints(y, x).piece
                if isinstance(piece, King) and piece.player == player:
                    return piece

    @classmethod
    def update_check_status(cls) -> None:
        pieces = GameManager.get_player_pieces(not cls.current_player)
        king = GameManager.get_king(cls.current_player)
        all_possible_moves = []
        for piece in pieces:
            all_possible_moves.extend(piece.get_all_possible_moves())
        cls.is_check = king.position in all_possible_moves

    @classmethod
    def check_mat(cls) -> bool:
        if not cls.is_check:
            return False
        king = GameManager.get_king(cls.current_player)
        possible_moves = king.remove_mating_moves(king.get_all_possible_moves())
        return len(possible_moves) == 0
