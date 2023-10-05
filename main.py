import tkinter as tk
from game_manager import GameManager
from clock_manager import ClockManager
from constants import *


def create_app() -> tk.Tk:
    root = tk.Tk()
    root.title("Chess")
    size_of_app = str(WIDTH_APP) + "x" + str(HEIGHT_APP)
    root.geometry(size_of_app)

    return root


def start_game(root: tk.Tk) -> None:
    canvas = tk.Canvas(root, width=WIDTH_APP, height=HEIGHT_APP)
    canvas.pack()

    ClockManager.create_timer(root, canvas)
    # Clock_Manager.create_notation_table(root, canvas)

    GameManager.create_board(root, canvas)
    GameManager.create_notation_table(root, canvas)
    GameManager.set_start_positions()

    root.mainloop()


if __name__ == "__main__":
    root = create_app()
    start_game(root)
