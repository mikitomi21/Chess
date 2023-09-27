import tkinter as tk
from game_manager import Game_Manager

def create_app() -> tk.Tk:
    root = tk.Tk()
    root.title("Chess")
    root.geometry("1280x800")

    return root

def start_game(root: tk.Tk) -> None:
    Game_Manager.create_board(root)
    Game_Manager.set_start_positions()
    root.mainloop()

if __name__ == "__main__":
    root = create_app()
    start_game(root)
