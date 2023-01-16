import progressbar
from dataclasses import dataclass, field
import time
from mlrgetpy.config.ConfigRep import ConfigRep
from mlrgetpy.util.Strutil import Strutil
import textwrap
from mlrgetpy.BoxDownload import BoxDownload


@dataclass
class MyProgressBar():
    fname: str = field()
    last: bool = field()
    # TODO : add to a config file
    short: str = field(default=ConfigRep.short_name)
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

        # download is not complete
        if downloaded < total_size:
            percentage = (downloaded / total_size)

            str_progress = self.__get_string_size(downloaded)
            self.__print_bar(name_wrap, percentage, str_progress)

            for name in name_wrap:
                print("\033[A", end="\r")

        # download is complete
        else:
            str_progress = self.__get_string_size(total_size)
            self.__print_bar(name_wrap, 1, str_progress)
            # self.pbar.finish()

    def __print_bar(self, name_wrap: list, perc, str_progress: str):
        tree = "├──"

        if self.last == True:
            tree = "└──"

        bdo = BoxDownload()
        first = True
        content = ""
        for name in name_wrap:
            if first:
                content = bdo.download_row(tree, name, str_progress, perc)
                first = False
            else:
                content += "\n"
                content += bdo.download_row2("│", name)

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
