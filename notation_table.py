import tkinter as tk
import os
from constants import *


class Notation_Table:
    def __init__(
        self,
        root: tk.Tk,
        canvas: tk.Canvas,
        player_time: int = PLAYER_WHITE,
    ):
        self.root = root
        self.player_time = player_time
        self.canvas = canvas

        self.table_of_moves: list[str] = []
        self.file_name: str = self.get_new_name_of_file()

        self.draw_table()

    def draw_table(self):
        self.canvas.create_rectangle(
            X_NT_START,
            Y_NT_START,
            X_NT_START + WIDTH_NT,
            Y_NT_START + HEIGHT_NT,
            fill=NT_COLOR,
        )

    def print_moves(self) -> None:
        with open(DIR_GAMES + self.file_name, "r") as file:
            print(file.read())

    def get_new_name_of_file(self) -> str:
        last_game = os.listdir("games/")[-1]
        new_game = str(int(last_game[:EXTENSION]) + 1) + ".txt"
        while len(new_game) < LENGHT_OF_NAME_OF_FILE:
            new_game = "0" + new_game

        with open(DIR_GAMES + new_game, "w"):
            pass
        return new_game

    def save_move_to_file(self, move: str) -> None:
        self.table_of_moves.append(move)
        with open(DIR_GAMES + self.file_name, "a") as file:
            file.write(move + " ")
