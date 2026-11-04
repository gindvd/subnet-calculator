import os
import shutil


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def get_terminal_size():
    return shutil.get_terminal_size()


def get_terminal_width():
    return shutil.get_terminal_size().columns


def get_terminal_height():
    return shutil.get_terminal_size().lines
    

def move_cursor(x, y):
    print(f"\033[{y};{x}H", end="")
