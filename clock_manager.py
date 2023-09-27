import tkinter as tk

from timer import Timer
from constants import *


class Clock_Manager:
    current_player = PLAYER_WHITE

    @classmethod
    def create_timer(cls, root, canvas):
        cls.timer = Timer(root, canvas, 10)
