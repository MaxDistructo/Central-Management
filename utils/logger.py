import colorama
from colorama import Fore, Style
import time


class Logger:
    func = ""

    def __init__(self, func_in: str):
        self.func = func_in

    def log(self, message: str, level: int):
        str_level = get_str_level(level)
        colorama.init()
        color = get_level_color(level)
        print(
            f'[{time.strftime("%H:%M:%S", time.localtime())}]{color}[{str_level}] [{self.func}] - {message}{Style.RESET_ALL}')

    def debug(self, message: str):
        self.log(message, 0)

    def info(self, message: str):
        self.log(message, 1)

    def warning(self, message: str):
        self.log(message, 2)

    def error(self, message: str):
        self.log(message, 3)

    def critical(self, message: str):
        self.log(message, 4)


def get_str_level(level: int) -> str:
    if level == 0:
        return "DEBUG"
    elif level == 1:
        return "INFO"
    elif level == 2:
        return "WARNING"
    elif level == 3:
        return "ERROR"
    elif level == 4:
        return "CRITICAL"
    else:
        raise IndexError


def get_level_color(level: int):
    if level == 0:
        return Fore.LIGHTYELLOW_EX
    elif level == 1:
        return Fore.WHITE
    elif level == 2:
        return Fore.YELLOW
    elif level == 3:
        return Fore.LIGHTRED_EX
    elif level == 4:
        return Fore.RED
    else:
        raise IndexError
