import tkinter as tk
from board import Board


def create_app():
    root = tk.Tk()
    root.title("Chess")
    root.geometry("1280x800")

    Board(root)

    root.mainloop()


if __name__ == "__main__":
    create_app()
