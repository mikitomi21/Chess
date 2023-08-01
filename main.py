import tkinter as tk
from constants import *
class Board:
    def __init__(self, root: tk.Tk):
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.is_clicked = False

        x1, y1 = 50, 50
        x2, y2 = 50 + LENGHT_OF_SQUARE, 50 + LENGHT_OF_SQUARE

        self.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

        self.canvas.tag_bind(self.rectangle, "<Button-1>", self.click_square)

    def click_square(self, event):
        if not self.is_clicked:
            self.canvas.itemconfig(self.rectangle, fill="red")
            self.is_clicked = True
        else:
            self.canvas.itemconfig(self.rectangle, fill="blue")
            self.is_clicked = False




def create_app():
    root = tk.Tk()
    root.title("Chess")
    root.geometry("1280x800")

    board = Board(root)

    root.mainloop()

if __name__ == "__main__":
    create_app()