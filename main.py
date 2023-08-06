import tkinter as tk
from board import Board


def create_app():
    root = tk.Tk()
    root.title("Chess")
    root.geometry("1280x800")

    board = Board(root)
    board.set_start_positions()
    root.mainloop()


if __name__ == "__main__":
    create_app()
