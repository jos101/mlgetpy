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
        self.short = ConfigRep.short_name

    def __call__(self, block_num, block_size, total_size):
        self.__num_calls += 1
        # if not self.pbar:
        #    self.pbar = progressbar.ProgressBar(maxval=total_size)

        #    self.pbar.start()
        size = 40
        downloaded = block_num * block_size

        bdo = BoxDownload()
        file_width = bdo.file_width() - 5
        name_wrap = []
        if self.short == True:
            name_wrap = [Strutil.shorten(self.fname, file_width)]
        else:
            name_wrap = textwrap.wrap(self.fname, file_width)

        # download is not complete
        # if downloaded < total_size:
        #     percentage = (downloaded / total_size)
        #
        #     str_progress = self.__get_string_size(downloaded)
        #     end = "\r"
        #     if len(name_wrap) == 1:
        #         end = "\r"
        #     self.__print_bar(name_wrap, percentage, str_progress, end=end)
        #
        #     # In jupyter notebook is not possible to move the cursor with
        #     # the ascii code "\033[A"
        #     # if len(name_wrap) > 1:
        #     #    for name in name_wrap:
        #     #         #move cursor one line up and in the begining of the line
        #     #        print("\033[A", end="\r")
        #
        # # download is complete
        # else:
        #     str_progress = self.__get_string_size(total_size)
        #     self.__print_bar(name_wrap, 1, str_progress, end="\n")
        #     # self.pbar.finish()

        str_progress = self.__get_string_size(downloaded)
        if total_size != -1:    
            if downloaded < total_size:
                percentage = (downloaded / total_size)
            else:
                percentage = 1
                str_progress = self.__get_string_size(total_size)
        else:
            percentage = 1.0
        
        self.__print_bar(name_wrap, percentage, str_progress, end="\r")
        # self.pbar.finish()

    def __print_bar(self, name_wrap: list, perc, str_progress: str, end="\n"):
        tree = "├──"

        if self.last == True:
            tree = "└──"

        bdo = BoxDownload()
        first = True
        content = ""
        if len(name_wrap) == 1:
            content = bdo.download_row(tree, name_wrap[0], str_progress, perc)
        elif len(name_wrap) > 1 and self.__num_calls == 1:
            count = 0
            for name in name_wrap:
                count += 1
                if first:
                    # content = bdo.download_row(tree, name, str_progress, perc)
                    content += bdo.download_row2(tree, name)
                    first = False
                else:
                    content += "\n"
                    # content += bdo.download_row2("│", name)
                    if count < len(name_wrap):
                        content += bdo.download_row("│  ",
                                                    name, str_progress, perc)
                    else:
                        content += bdo.download_row("│  ",
                                                    name, str_progress, perc)
        elif len(name_wrap) > 1 and self.__num_calls > 1:
            content += bdo.download_row("│  ",
                                        name_wrap[-1], str_progress, perc)

        print(f"{content}", end=end)

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
