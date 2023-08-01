import unittest
import tkinter as tk

from main import Board
from constants import *

class Test_gui(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.geometry("1280x800")
        self.board = Board(self.root)

    def test_changing_color_of_square_after_click(self):
        initial_color = self.board.squares[0][0].canvas.itemcget(self.board.squares[0][0].rectangle, "fill")
        self.assertEqual("blue", initial_color)

        self.board.squares[0][0].click_square(None)

        initial_color = self.board.squares[0][0].canvas.itemcget(self.board.squares[0][0].rectangle, "fill")
        self.assertEqual("red", initial_color)

        self.board.squares[0][0].click_square(None)

        initial_color = self.board.squares[0][0].canvas.itemcget(self.board.squares[0][0].rectangle, "fill")
        self.assertEqual("blue", initial_color)

    def test_correct_take_position_on_square(self):
        output = self.board.squares[0][0].click_square(None)
        self.assertEqual("a8", output)

        output = self.board.squares[0][SIZE_OF_BOARD-1].click_square(None)
        self.assertEqual("h8", output)

        output = self.board.squares[SIZE_OF_BOARD-1][SIZE_OF_BOARD-1].click_square(None)
        self.assertEqual("h1", output)

        output = self.board.squares[SIZE_OF_BOARD-1][0].click_square(None)
        self.assertEqual("a1", output)

