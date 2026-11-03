import os
import shutil


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def get_terminal_size():
    return shutil.get_terminal_siz


def move_cursor(x, y):
    print(f"\033[{y};{x}H", end="")
