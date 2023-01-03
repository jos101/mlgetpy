import progressbar
from dataclasses import dataclass, field
import time
from mlrgetpy.util.Strutil import Strutil


@dataclass
class MyProgressBar():
    fname: str = field()
    last: bool = field()

    def __post_init__(self) -> None:
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        # if not self.pbar:
        #    self.pbar = progressbar.ProgressBar(maxval=total_size)

        #    self.pbar.start()
        size = 40
        downloaded = block_num * block_size
        if downloaded < total_size:
            # self.pbar.update(downloaded)
            # print("-----", end="\r")
            perc = int((downloaded / total_size)*size)
            self.__print_bar(perc, size, downloaded, total_size)
        else:
            self.__print_bar(size, size, total_size, total_size)
            # self.pbar.finish()
            print()

    def __print_bar(self, perc, size, downloaded, total_size):
        t_down = "━" * perc
        t_ream = " " * (size - perc)
        str_downloaded = self.__get_string_size(downloaded)
        str_total_size = self.__get_string_size(total_size)
        str_progress = ""
        tree = "├──"

        if self.last == True:
            tree = "└──"

        # time.sleep(0.2)
        if downloaded != total_size:
            str_progress = f"({str_downloaded})"
        else:
            str_progress = f"({str_total_size})"

        # TODO: create function
        # shorten the name file if necessary
        name = Strutil.shorten(self.fname, 18)

        content = f"{tree}{name:20s} {str_progress:10s} [{t_down}{t_ream}] { int(perc/size*100)}%"
        content = f"│{content:90s}│"
        print(
            f"{content}", end="\r")

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
