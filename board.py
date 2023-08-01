from constants import *
import tkinter as tk
class Square:
    def __init__(self, canvas: tk.Canvas, row: int, col: int):
        self.canvas = canvas
        self.row = row
        self.col = col
        self.color = self.get_color()

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

    def click_square(self, event) -> str:
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

        return f"{chr(97+self.row)}{8-self.col}"

class Board:
    def __init__(self, root: tk.Tk):
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.squares = self.create_squares()

    def create_squares(self) -> list[Square]:
        squares = []
        for col in range(SIZE_OF_BOARD):
            row_of_squares = []
            for row in range(SIZE_OF_BOARD):
                row_of_squares.append(Square(self.canvas, row, col))
            squares.append(row_of_squares)
        return squares
