import tkinter as tk

from timer import Timer
<<<<<<< HEAD
from notation_table import Notation_Table
=======
>>>>>>> 66c3da8 (Add place for timer)
from constants import *


class Clock_Manager:
    current_player = PLAYER_WHITE

    @classmethod
    def create_timer(cls, root, canvas):
        cls.timer = Timer(root, canvas, 10)
<<<<<<< HEAD

    @classmethod
    def create_notation_table(cls, root, canvas):
        cls.notation_table = Notation_Table(root, canvas)
=======
>>>>>>> 66c3da8 (Add place for timer)
