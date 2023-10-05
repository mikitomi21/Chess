import tkinter as tk

from timer import Timer
from notation_table import NotationTable
from constants import *


class ClockManager:
    current_player = PLAYER_WHITE

    @classmethod
    def create_timer(cls, root, canvas):
        cls.timer = Timer(root, canvas, 10)

    @classmethod
    def create_notation_table(cls, root, canvas):
        cls.notation_table = NotationTable(root, canvas)
        # cls.notation_table.save_moves_to_file()
