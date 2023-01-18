from dataclasses import dataclass, field
import textwrap
import os


@dataclass
class BoxDownload:
    """A class to create the download box. The width adapts to the size of the terminal


        Top            ┌────────────────────────────────────────────────────────────────────┐

        Header         │53_[Iris]                                                           │

        Separator      ├────────────────────────────────────────────────────────────────────┤

        text row       │https://archive.ics.uci.edu/ml/machine-learning-databases/iris/     │

        download row   │├──Index                   105.0 bytes   [━━━━━━━━━━━━━━━━━━]100%   │

        download row   │├──bezdekIris.data         4.4 KB        [━━━━━━━━━━━━━━━━━━]100%   │

        download row   │├──iris.data               4.4 KB        [━━━━━━━━━━━━━━━━━━]100%   │

        download row   │└──iris.names              2.9 KB        [━━━━━━━━━━━━━━━━━━]100%   │

        bottom         └────────────────────────────────────────────────────────────────────┘

        Args:
            width (str): the width of the box
            autoresize (bool): if True will change the width with the size of the terminal

    """

    width: int = field(default=70)
    autoresize: bool = field(default=True)
    __text_width = 0
    __progress_bar_width = 0
    __str_progress = 0
    __perc_width = 0
    __file_width = 0

   # TODO Tests
    def __post_init__(self) -> None:
        self.calc_sizes()

    def calc_sizes(self):
        """Change the width of the box based on the terminal size
        """
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

    def download_row(self, prefile: str, file: str, str_progress: str, percentage: float) -> str:
        """Create a string of a row with the download file

        │├──iris.data               4.4 KB        [━━━━━━━━━         ]50%    │

        prefile         : ├──
        file            : iris.data
        str_progress_bar: 4.4 KB
        progress bar    : [━━━━━━━━━         ]
        percentage: 50%

        Args:
            prefile (str): text before the file name
            file (str): the file name
            str_progress (str): the total downloaded so far (10 bytes, 10 kB, 100 GB, etc)
            percentage (float): the percentage downloaded so far

        Raises:
            ValueError: the percentage must be a float value between 0 and 1, inclusive

        Returns:
            str: a row of a table
            i.e:
            │├──iris.data               4.4 KB        [━━━━━━━━━         ]50%    │

        """
        self.calc_sizes()

        if percentage > 1 or percentage < 0:
            raise ValueError(
                "Percentage should be a  value between 0 and 1, inclusive")

        file = file.ljust(self.__file_width - len(prefile), ' ')
        str_progress = str_progress.ljust(self.__str_progress, ' ')

        progress_bar = self.progress_bar(percentage, self.__progress_bar_width)

        perc_str = str(round(percentage * 100)) + "%"
        perc_str = perc_str.ljust(self.__perc_width, ' ')

        string = f"│{prefile}{file}{str_progress}{progress_bar}{perc_str}│"

        return string

    def progress_bar(self, percentage: float, width: int) -> str:
        """Create a progress bar

        i.e: progress_bar(0.6, 15) -> [━━━━━━━━     ]

        Args:
            percentage (float): value between 0 and 1, inclusive
            width (int): the width of the progress bar

        Raises:
            ValueError: Percentage should be a  value between 0 and 1, inclusive

        Returns:
            str: the progress bar in ascii
        """
        if percentage > 1 or percentage < 0:
            raise ValueError(
                "Percentage should be a  value between 0 and 1, inclusive")

        total_bars = (width - 2)
        num1 = round(percentage * total_bars)
        num2 = total_bars - num1

        total_download = "━" * num1
        total_remaining = " " * num2

        progress_bar = "[" + total_download + total_remaining + "]"

        return progress_bar

    def download_row2(self, left: str, right: str):
        """Create a row divided in two parts (left and right)

        The concatenation of the left and right part are padded with the
        text_width. If the right part does not fit, it is wrap in the next lines.
        The left part will add spaces.

        Diference between download_row and download_row2:

        ┌download_row("├──", "GooglePlus_Microso", "6490.7 KB", 1.0)

        │

        └──> │├──GooglePlus_Microso      6490.7 KB     [━━━━━━━━━━━━━━━━━━]100%   │

        ┌──> ││ft.csv                                                             │  

        │

        └download_row2("│", "ft.csv")                                                                                  │


        In this case will wrap the right part to fit the text witdh  and add 3 spaces in the next line 

        download_row2( "├──", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod")

        │├──Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do  │

        │   eiusmod                                                          │

         ^^^

        Args:
            left (str): left part of the rows. Uses character from the text width
            right (str): the text of the row. Uses character from the text width

        Returns:
            _type_: the row in ascii
        """

        self.calc_sizes()

        left_width = len(left)
        right_width = self.__text_width - left_width

        new_text = ""
        right_list = textwrap.wrap(right, right_width)
        left_list = [left]

        i = 0
        first = True
        while i < len(right_list):
            left_text = " "
            if first:
                left_text = left
                first = False
            else:
                new_text += "\n"

            right_text = right_list[i].ljust(right_width, ' ')
            left_text = left_text.ljust(left_width, ' ')
            new_text += "│" + left_text + right_text + "│"

            i += 1

        return new_text

    def download_row3(self, left: str, right: str, left_width: int = 5) -> str:
        """Similar to download_row2 but defines a fix padding in the left side


        Diference between download_row2 and download_row3:

        ┌download_row3("│", "ft.csv)

        │

        └──> ││    ft.csv                                                         │

        ┌──> ││ft.csv                                                             │  

        │

        └download_row2("│", "ft.csv)                                                                                  │




        Args:
            left (str): left part of the rows. Uses character from the text width
            right (str): the text of the row. Uses character from the text width
            left_width (int, optional): Pads with spaces the left part. Defaults to 5.

        Returns:
            str: the row in ascii
        """

        self.calc_sizes()
        right_width = self.__text_width - left_width

        left_list = textwrap.wrap(left, left_width)
        right_list = textwrap.wrap(right, right_width)

        i = 0
        text = ""
        first = True
        while i < len(left_list) or i < len(right_list):
            if first:
                first = False
            else:
                text += "\n"

            text_left = ""
            text_right = ""
            if i < len(left_list):
                text_left = left_list[i].ljust(left_width, ' ')
            else:
                text_left = str(" ").ljust(left_width, ' ')

            if i < len(right_list):
                text_right = right_list[i].ljust(right_width, ' ')
            else:
                text_right = str(" ").ljust(right_width, ' ')

            text += "│" + text_left + text_right + "│"

            i += 1

        return text

    def top(self) -> str:
        """Create the top part of the box in ascii

        Returns:
            str: the top part of the box in ascii
        """

        self.calc_sizes()
        return "┌" + "─" * (self.__text_width) + "┐"

    def header(self, text: str) -> str:
        """Create the header part of the box

        Args:
            text (str): the text in the header

        Returns:
            str: the header row in ascii
        """

        self.calc_sizes()
        new_text = ""
        text_list = textwrap.wrap(text, self.__text_width)

        i = 0
        first = True
        while i < len(text_list):
            if first:
                first = False
            else:
                new_text += "\n"

            new_text += "│" + text_list[i].ljust(self.__text_width, ' ') + "│"

            i += 1

        return new_text

    def row_sep(self) -> str:
        """Create the row separator of the box in ascii

        Returns:
            str: the row separator of the box in ascii
        """
        self.calc_sizes()
        return "├" + "─" * (self.__text_width) + "┤"

    def bottom(self) -> str:
        """Create the bottom part of the box in ascii

        Returns:
            str: the bottom part of the box in ascii
        """
        self.calc_sizes()
        return "└" + "─" * (self.__text_width) + "┘"

    def text_row(self, text: str) -> str:
        """Create a row in the box with a text

        The text will be wrap if is greater than the with of the box

        Args:
            text (str): The text to be in the row

        Returns:
            str: the row in ascii
        """

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

    def file_width(self) -> int:
        return self.__file_width
