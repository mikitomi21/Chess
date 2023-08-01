import unittest
import tkinter as tk
from main import Board
class Test_gui(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.geometry("1280x800")
        self.board = Board(self.root)

    def test_color_of_square_chang_after_click(self):
        initial_color = self.board.canvas.itemcget(self.board.rectangle, "fill")
        self.assertEqual(initial_color, "blue")

        self.board.click_square(None)

        initial_color = self.board.canvas.itemcget(self.board.rectangle, "fill")
        self.assertEqual(initial_color, "red")

        self.board.click_square(None)

        initial_color = self.board.canvas.itemcget(self.board.rectangle, "fill")
        self.assertEqual(initial_color, "blue")

