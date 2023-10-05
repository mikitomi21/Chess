import copy

from constants import *
import tkinter as tk
from PIL import Image, ImageTk

from point import Point


class Circle:
    def __init__(self, canvas: tk.Canvas, y, x, square):
        self.canvas = canvas
        self.y = y
        self.x = x
        self.square = square

    def create_oval(self) -> None:
        circle = self.canvas.create_oval(
            START_X + LENGTH_OF_SQUARE * self.x + SIZE_OF_CIRCLE,
            START_Y + LENGTH_OF_SQUARE * self.y + SIZE_OF_CIRCLE,
            START_X + LENGTH_OF_SQUARE * (self.x + 1) - SIZE_OF_CIRCLE,
            START_Y + LENGTH_OF_SQUARE * (self.y + 1) - SIZE_OF_CIRCLE,
            fill="red",
        )
        self.canvas.tag_bind(circle, "<Button-1>", self.square.click_piece)


class Square:
    def __init__(self, root: tk.Tk, canvas: tk.Canvas, row: int, col: int):
        self.root = root
        self.canvas = canvas
        self.row = row
        self.col = col
        self.color = self.get_color()
        self.piece = None

        self.draw_square()

        self.image_path = None
        self.image = None

        self.draw_image()

    def draw_square(self):
        x1 = START_X + LENGTH_OF_SQUARE * self.row
        y1 = START_Y + LENGTH_OF_SQUARE * self.col
        x2 = START_X + LENGTH_OF_SQUARE * (self.row + 1)
        y2 = START_Y + LENGTH_OF_SQUARE * (self.col + 1)

        self.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)
        self.canvas.tag_bind(self.rectangle, "<Button-3>", self.click_square)
        self.canvas.tag_bind(self.rectangle, "<Button-1>", self.click_piece)

    def show_possible_moves(self, piece):
        from game_manager import GameManager

        possible_moves = piece.remove_mating_moves(piece.get_all_possible_moves())
        for pos in possible_moves:
            y, x = Point.get_position(pos)
            Circle(
                self.canvas,
                y,
                x,
                GameManager.board.get_square(Point.get_position_int(y, x)),
            ).create_oval()

    def click_piece(self, event) -> None:
        # print(f"{chr(97 + self.row)}{8 - self.col}")
        from game_manager import GameManager

        GameManager.board.draw_board()

        if self.piece and self.piece.player == GameManager.get_player():
            self.show_possible_moves(self.piece)

        if (
            GameManager.get_selected_piece() is None
            or GameManager.get_player() != GameManager.selected_piece.player
        ):
            GameManager.set_selected_piece(self.piece)
            GameManager.set_selected_square(self)
        else:
            GameManager.try_move_piece(self)

    def load_image(self):
        image = Image.open(self.image_path)
        image = image.resize(
            (SIZE_OF_PIECE - MARGIN_OF_PIECE, SIZE_OF_PIECE - MARGIN_OF_PIECE)
        )

        self.photo = ImageTk.PhotoImage(image)

        img_x = START_X + LENGTH_OF_SQUARE * self.row + MARGIN_OF_PIECE / 2
        img_y = START_Y + LENGTH_OF_SQUARE * self.col + MARGIN_OF_PIECE / 2
        self.image = self.canvas.create_image(
            img_x, img_y, image=self.photo, anchor=tk.NW
        )
        self.canvas.tag_bind(self.image, "<Button-3>", self.click_square)
        self.canvas.tag_bind(self.image, "<Button-1>", self.click_piece)

    def set_image_path(self, image_path: str) -> None:
        self.image_path = image_path
        if image_path:
            self.load_image()

    def get_image_path(self) -> str:
        return self.image_path

    def draw_image(self) -> None:
        if self.image_path:
            self.load_image()

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

    def __deepcopy__(self, memo):
        new_square = self.__class__(self.root, self.canvas, self.row, self.col)
        new_square.color = self.color
        new_square.piece = copy.deepcopy(self.piece, memo)
        new_square.image_path = self.image_path
        new_square.image = self.image
        return new_square


class Board:
    def __init__(self, root: tk.Tk, canvas: tk.Canvas):
        self.root = root
        self.canvas = canvas
        self.squares = self.create_squares()

    def create_squares(self) -> list[list[Square]]:
        squares = []
        for col in range(SIZE_OF_BOARD):
            row_of_squares = []
            for row in range(SIZE_OF_BOARD):
                row_of_squares.append(Square(self.root, self.canvas, row, col))
            squares.append(row_of_squares)
        return squares

    def draw_board(self) -> None:
        for y in range(SIZE_OF_BOARD):
            for x in range(SIZE_OF_BOARD):
                square = self.get_square_ints(y, x)
                square.draw_square()
                square.draw_image()

    @staticmethod
    def draw_pieces(squares: list[Square]) -> None:
        for square in squares:
            square.draw_square()
            square.draw_image()

    def get_square(self, pos: str) -> Square:
        y, x = Point.get_position(pos)
        return self.squares[y][x]

    def get_square_ints(self, y: int, x: int) -> Square:
        return self.squares[y][x]

    def __deepcopy__(self, memo):
        if self in memo:
            return memo[self]
        new_board = self.__class__(self.root, self.canvas)
        new_board.squares = []
        memo[self] = new_board

        for row in self.squares:
            new_row = []
            for square in row:
                new_square = copy.deepcopy(square, memo)
                new_row.append(new_square)
            new_board.squares.append(new_row)

        return new_board
