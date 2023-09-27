import tkinter as tk
from constants import *


class Notation_Table:
    def __init__(
        self,
        root: tk.Tk,
        canvas: tk.Canvas,
        player_time: int = PLAYER_WHITE,
    ):
        self.root = root
        self.player_time = player_time
        self.canvas = canvas

        self.draw_table()

    def draw_table(self):
        self.canvas.create_rectangle(
            X_NT_START,
            Y_NT_START,
            X_NT_START + WIDTH_NT,
            Y_NT_START + HEIGHT_NT,
            fill=NT_COLOR,
        )
