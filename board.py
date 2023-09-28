from constants import *
import tkinter as tk
from PIL import Image, ImageTk

from point import Point


class Cirle:
    def __init__(self, canvas: tk.Canvas, y, x, square):
        self.canvas = canvas
        self.y = y
        self.x = x
        self.square = square

    def create_oval(self) -> None:
        circle = self.canvas.create_oval(
            START_X + LENGHT_OF_SQUARE * self.x + SIZE_OF_CIRCLE,
            START_Y + LENGHT_OF_SQUARE * self.y + SIZE_OF_CIRCLE,
            START_X + LENGHT_OF_SQUARE * (self.x + 1) - SIZE_OF_CIRCLE,
            START_Y + LENGHT_OF_SQUARE * (self.y + 1) - SIZE_OF_CIRCLE,
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
        x1 = START_X + LENGHT_OF_SQUARE * self.row
        y1 = START_Y + LENGHT_OF_SQUARE * self.col
        x2 = START_X + LENGHT_OF_SQUARE * (self.row + 1)
        y2 = START_Y + LENGHT_OF_SQUARE * (self.col + 1)

        self.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)
        self.canvas.tag_bind(self.rectangle, "<Button-3>", self.click_square)
        self.canvas.tag_bind(self.rectangle, "<Button-1>", self.click_piece)

    def show_possible_moves(self, piece):
        from game_manager import Game_Manager

        possible_moves = piece.get_all_possible_moves()
        for pos in possible_moves:
            y, x = Point.get_position(pos)
            Cirle(
                self.canvas,
                y,
                x,
                Game_Manager.board.get_square(Point.get_position_int(y, x)),
            ).create_oval()

    def click_piece(self, event) -> None:
        # print(f"{chr(97 + self.row)}{8 - self.col}")
        from game_manager import Game_Manager

        Game_Manager.board.draw_board(Game_Manager.board)

        if self.piece and self.piece.player == Game_Manager.get_player():
            self.show_possible_moves(self.piece)

        if (
            Game_Manager.get_selected_piece() is None
            or Game_Manager.get_player() != Game_Manager.selected_piece.player
        ):
            Game_Manager.set_selected_piece(self.piece)
            Game_Manager.set_selected_square(self)
        else:
            Game_Manager.try_move_piece(self)

    def load_image(self):
        image = Image.open(self.image_path)
        image = image.resize((100, 100))

        self.photo = ImageTk.PhotoImage(image)

        img_x = START_X + LENGHT_OF_SQUARE * self.row
        img_y = START_Y + LENGHT_OF_SQUARE * self.col
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


class Board:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.squares = self.create_squares()

    def create_squares(self) -> list[Square]:
        squares = []
        for col in range(SIZE_OF_BOARD):
            row_of_squares = []
            for row in range(SIZE_OF_BOARD):
                row_of_squares.append(Square(self.root, self.canvas, row, col))
            squares.append(row_of_squares)
        return squares

    def draw_board(self, board) -> None:
        for y in range(SIZE_OF_BOARD):
            for x in range(SIZE_OF_BOARD):
                square = board.get_square_ints(y, x)
                square.draw_square()
                square.draw_image()

    def draw_pieces(self, squares: list[Square]) -> None:
        for square in squares:
            square.draw_square()
            square.draw_image()

    def get_square(self, pos: str) -> Square:
        y, x = Point.get_position(pos)
        return self.squares[y][x]

    def get_square_ints(self, y: int, x: int) -> Square:
        return self.squares[y][x]
