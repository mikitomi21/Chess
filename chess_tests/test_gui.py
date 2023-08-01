import unittest
import tkinter as tk
from main import Board
class Test_gui(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.geometry("1280x800")
        self.board = Board(self.root)

    def test_changing_color_of_square_after_click(self):
        initial_color = self.board.squares[0][0].canvas.itemcget(self.board.squares[0][0].rectangle, "fill")
        self.assertEqual(initial_color, "blue")

        self.board.squares[0][0].click_square(None)

        initial_color = self.board.squares[0][0].canvas.itemcget(self.board.squares[0][0].rectangle, "fill")
        self.assertEqual(initial_color, "red")

        self.board.squares[0][0].click_square(None)

        initial_color = self.board.squares[0][0].canvas.itemcget(self.board.squares[0][0].rectangle, "fill")
        self.assertEqual(initial_color, "blue")

