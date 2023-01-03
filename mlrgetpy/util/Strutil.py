from typing import List

from sympy import false, true
import math


class Strutil:

    def get_list(text: str, sep: str = " ", width=10):
        buffer: str = ""
        text_list: List = []

        first = true
        for (i, word) in enumerate(text.split(sep)):
            prev_buffer = buffer
            if i == 0 and len(text.split(sep)) == 1:
                buffer = word
                prev_buffer = word
            elif i == 0 and len(text.split(sep)) > 1:
                buffer = word + sep
                prev_buffer = word + sep
            elif i < (len(text.split(sep)) - 1):
                buffer += word + sep
            else:
                buffer += word

            if len(buffer) > width and first == False:
                if len(prev_buffer) > width and sep == ",":
                    text_list += Strutil.get_list(prev_buffer, " ")
                else:
                    text_list.append(prev_buffer)

                if i < (len(text.split(sep)) - 1):
                    buffer = word.lstrip() + sep
                else:
                    buffer = word.lstrip()

            first = False

        if len(buffer) > width and sep == " ":
            #text_list += Strutil.get_list(buffer, " ")
            text_list.append(buffer[0:width-3] + "...")
        elif len(buffer) > width and sep == ",":
            text_list += Strutil.get_list(buffer, " ")
        else:
            text_list.append(buffer)

        return text_list

    def get_max_length(li1: List, li2: List):
        return max([len(li1), len(li2)])

    def get_value(li: List, idx):
        value: str = ""
        if idx < len(li):
            value = li[idx]

        return value

    def left(fname, size: int = 18, pad="[...]") -> str:
        if len(fname) < size:
            return fname

        num = (size - len(pad)) / 2
        if (num % 2) != 0:
            num += 1
        num = math.floor(num)

        return fname[0:num]

    def right(fname, size: int = 18, pad="[...]") -> str:
        if len(fname) < size:
            return fname

        num = (size - len(pad)) / 2
        num = math.floor(num)

        index1 = len(fname) - num

        return fname[index1:]

    def shorten(fname, size: int = 18, pad="[...]"):
        if len(fname) < size:
            return fname

        return Strutil.left(fname, size, pad) + pad + Strutil.right(fname, size, pad)
