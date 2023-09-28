import tkinter as tk

from timer import Timer
from notation_table import Notation_Table
from constants import *


class Clock_Manager:
    current_player = PLAYER_WHITE

    @classmethod
    def create_timer(cls, root, canvas):
        cls.timer = Timer(root, canvas, 10)

    @classmethod
    def create_notation_table(cls, root, canvas):
        cls.notation_table = Notation_Table(root, canvas)