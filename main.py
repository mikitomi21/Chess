import tkinter as tk

def create_board():
    root = tk.Tk()
    root.title("Chess")
    root.geometry("1280x800")

    label = tk.Label(root, text="Hello, World!")
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    create_board()