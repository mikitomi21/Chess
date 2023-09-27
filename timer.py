from constants import *
import tkinter as tk
from time import time


class Timer:
    def __init__(
        self, root: tk.Tk, canvas: tk.Canvas, player_time: int, increment: int = 0
    ):
        self.root = root
        self.player_time = player_time
        self.increment = increment
        self.current_player = PLAYER_WHITE
        self.canvas = canvas

        self.draw_timer()

    def draw_timer(self):
        self.canvas.create_rectangle(
            X_TIMER_START,
            Y_TIMER_START_1,
            X_TIMER_START + WIDTH_TIMER,
            Y_TIMER_START_1 + HEIGHT_TIMER,
            fill=TIMER_COLOR,
        )

        self.canvas.create_rectangle(
            X_TIMER_START,
            Y_TIMER_START_2,
            X_TIMER_START + WIDTH_TIMER,
            Y_TIMER_START_2 + HEIGHT_TIMER,
            fill=TIMER_COLOR,
        )

    def click_square(self):
        pass

    @classmethod
    def next_player(cls):
        if cls.current_player == PLAYER_WHITE:
            cls.current_player = PLAYER_BLACK
        else:
            cls.current_player = PLAYER_WHITE
