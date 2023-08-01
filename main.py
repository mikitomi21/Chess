import tkinter as tk
from constants import *

class Square:
    def __init__(self, canvas: tk.Canvas, row: int, col: int):
        self.canvas = canvas
        self.is_clicked = False
        self.row = row
        self.col = col

        x1, y1 = START_X + LENGHT_OF_SQUARE * row, START_Y + LENGHT_OF_SQUARE * col
        x2, y2 = START_X + LENGHT_OF_SQUARE * (row+1), START_Y + LENGHT_OF_SQUARE * (col+1)

        self.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

        self.canvas.tag_bind(self.rectangle, "<Button-1>", self.click_square)

    def click_square(self, event) -> str:
        if not self.is_clicked:
            self.canvas.itemconfig(self.rectangle, fill="red")
            self.is_clicked = True
        else:
            self.canvas.itemconfig(self.rectangle, fill="blue")
            self.is_clicked = False
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






def create_app():
    root = tk.Tk()
    root.title("Chess")
    root.geometry("1280x800")

    board = Board(root)

    root.mainloop()

if __name__ == "__main__":
    create_app()