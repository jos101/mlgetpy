from dataclasses import dataclass
import textwrap
import os


@dataclass
class BoxDownload:

    width: int = 70
    autoresize: bool = True
    __text_width = 0
    __progress_bar_width = 0
    __str_progress = 0
    __perc_width = 0
    __file_width = 0

   # TODO Tests
    def __post_init__(self) -> None:
        self.calc_sizes()

    def calc_sizes(self):
        if self.autoresize:
            size = os.get_terminal_size()
            if size.columns > 90:
                self.width = 90
            elif size.columns > 70:
                self.width = 70
            elif size.columns > 50:
                self.width = 50
            else:
                self.width = 50

        self.__text_width = self.width - 2
        self.__progress_bar_width = round(self.__text_width * 0.3)
        self.__str_progress = round(self.__text_width * 0.2)
        self.__perc_width = round(self.__text_width * 0.1)
        self.__file_width = round(self.__text_width * 0.4)

    def download_row(self, tree, file, str_progress, perc: float):
        self.calc_sizes()

        if perc > 1 or perc < 0:
            raise ValueError(
                "Percentage should be a  value between 0 and 1, inclusive")

        file = file.ljust(self.__file_width - len(tree), ' ')
        str_progress = str_progress.ljust(self.__str_progress, ' ')

        total_bars = (self.__progress_bar_width - 2)
        num1 = round(perc * total_bars)
        num2 = total_bars - num1
        t_down = "━" * num1
        t_ream = " " * num2

        progress_bar = "[" + t_down + t_ream + "]"

        perc_str = str(round(perc * 100)) + "%"
        perc_str = perc_str.ljust(self.__perc_width, ' ')

        string = f"│{tree}{file}{str_progress}{progress_bar}{perc_str}│"

        return string

    def download_row2(self, tree, file):
        self.calc_sizes()

        text = "│" + tree + file + "│"
        text = text.ljust(self.__file_width, ' ')

        return text

    def download_row3(self, left, right, left_width=5):
        self.calc_sizes()

        left2 = left.ljust(left_width, ' ')
        right2 = right.ljust(self.__text_width - left_width, ' ')

        text = "│" + left2 + right2 + "│"

        return text

    def top(self):
        self.calc_sizes()
        return "┌" + "─" * (self.__text_width) + "┐"

    def header(self, text: str) -> str:
        self.calc_sizes()
        text = text.ljust(self.__text_width, ' ')
        return f'│{text}│'

    def row_sep(self):
        self.calc_sizes()
        return "├" + "─" * (self.__text_width) + "┤"

    def bottom(self):
        self.calc_sizes()
        return "└" + "─" * (self.__text_width) + "┘"

    def text_row(self, text: str) -> str:
        self.calc_sizes()
        new_text = ""
        first = True
        for item in textwrap.wrap(text, self.__text_width):
            temp = "│" + item.ljust(self.__text_width, ' ') + "│"
            if first == True:
                new_text = temp
                first = False
            else:
                new_text += "\n" + temp

        return new_text
