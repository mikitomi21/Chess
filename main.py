import tkinter as tk
from game_manager import Game_Manager
from clock_manager import Clock_Manager
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

    Clock_Manager.create_timer(root, canvas)
    # Clock_Manager.create_notation_table(root, canvas)

    Game_Manager.create_board(root, canvas)
    Game_Manager.create_notation_table(root, canvas)
    Game_Manager.set_start_positions()

    root.mainloop()


if __name__ == "__main__":
    root = create_app()
    start_game(root)
