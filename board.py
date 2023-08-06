from constants import *
import tkinter as tk
from point import Point
from chess_pieces.piece import Piece
from chess_pieces.bishop import Bishop
from chess_pieces.king import King
from chess_pieces.knight import Knight
from chess_pieces.pawn import Pawn
from chess_pieces.queen import Queen
from chess_pieces.rook import Rook


class Square:
    def __init__(self, canvas: tk.Canvas, row: int, col: int):
        self.canvas = canvas
        self.row = row
        self.col = col
        self.color = self.get_color()
        self.piece = None

        x1 = START_X + LENGHT_OF_SQUARE * row
        y1 = START_Y + LENGHT_OF_SQUARE * col
        x2 = START_X + LENGHT_OF_SQUARE * (row + 1)
        y2 = START_Y + LENGHT_OF_SQUARE * (col + 1)

        self.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)

        self.canvas.tag_bind(self.rectangle, "<Button-1>", self.click_square)

    def get_color(self) -> str:
        if (self.row + self.col) % 2:
            return BLACK
        return WHITE

    def click_square(self, event) -> None:
        if self.color == WHITE:
            self.canvas.itemconfig(self.rectangle, fill=WHITE_PICKED)
            self.color = WHITE_PICKED
        elif self.color == WHITE_PICKED:
            self.canvas.itemconfig(self.rectangle, fill=WHITE)
            self.color = WHITE
        elif self.color == BLACK:
            self.canvas.itemconfig(self.rectangle, fill=BLACK_PICKED)
            self.color = BLACK_PICKED
        elif self.color == BLACK_PICKED:
            self.canvas.itemconfig(self.rectangle, fill=BLACK)
            self.color = BLACK

        if self.piece:
            print(
                f"{chr(97+self.row)}{8-self.col}: {self.piece} Player-{self.piece.player}"
            )
        else:
            print(f"{chr(97 + self.row)}{8 - self.col}")


class Board:
    def __init__(self, root: tk.Tk):
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.squares = self.create_squares()

    def set_start_positions(self) -> None:
        Piece.set_board(self)
        Bishop.set_start_positions()
        King.set_start_positions()
        Knight.set_start_positions()
        Pawn.set_start_positions()
        Queen.set_start_positions()
        Rook.set_start_positions()

    def create_squares(self) -> list[Square]:
        squares = []
        for col in range(SIZE_OF_BOARD):
            row_of_squares = []
            for row in range(SIZE_OF_BOARD):
                row_of_squares.append(Square(self.canvas, row, col))
            squares.append(row_of_squares)
        return squares

    def get_square(self, position: str) -> Square:
        position = Point(position)
        y, x = position.y, position.x
        return self.squares[y][x]
