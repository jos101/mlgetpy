import progressbar
from dataclasses import dataclass, field
import time
from mlrgetpy.util.Strutil import Strutil
import textwrap


@dataclass
class MyProgressBar():
    fname: str = field()
    last: bool = field()
    short: str = field(default=True)
    __num_calls = 0

    def __post_init__(self) -> None:
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        self.__num_calls += 1
        # if not self.pbar:
        #    self.pbar = progressbar.ProgressBar(maxval=total_size)

        #    self.pbar.start()
        size = 40
        downloaded = block_num * block_size

        name_wrap = []
        if self.short == True:
            name_wrap = [Strutil.shorten(self.fname, 18)]
        else:
            name_wrap = textwrap.wrap(self.fname, 18)

        #download is not complete
        if downloaded < total_size:
            perc = int((downloaded / total_size)*size)

            str_progress = self.__get_string_size(downloaded)
            self.__print_bar(name_wrap, perc, size, downloaded,
                             total_size, str_progress)

            for name in name_wrap:
                print("\033[A", end="\r")

        # download is complete
        else:
            str_progress = self.__get_string_size(total_size)
            self.__print_bar(name_wrap, size, size, total_size,
                             total_size, str_progress)
            # self.pbar.finish()

    def __print_bar(self, name_wrap: list, perc, size, downloaded, total_size, str_progress: str):
        t_down = "━" * perc
        t_ream = " " * (size - perc)
        tree = "├──"

        if self.last == True:
            tree = "└──"

        first = True
        content = ""
        for name in name_wrap:
            if first:
                content = f"{tree}{name:20s} {str_progress:10s} [{t_down}{t_ream}] { int(perc/size*100)}%"
                content = f"│{content:90s}│"
                first = False
            else:
                content += "\n"
                content += f"││  {name:87}│"

        print(f"{content}")

    def __get_string_size(self, downloaded):
        kbs = downloaded / 1024
        mbs = kbs / 1024
        gbs = mbs / 1024

        str = f"{downloaded:.1f} bytes"
        if (int(kbs) > 0):
            str = f"{kbs:.1f} KB"
        elif (int(mbs) > 0):
            str = f"{mbs:.1f} MB"
        elif (int(gbs) > 0):
            str = f"{gbs:.1f} GB"

        return str
