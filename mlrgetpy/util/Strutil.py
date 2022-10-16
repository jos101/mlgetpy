from typing import List

from sympy import false, true


class Strutil:

    def get_list(text: str, sep: str = " ", width=10):
        buffer: str = ""
        text_list: List = []

        first = true
        for word in text.split(sep):
            prev_buffer = buffer
            if buffer == "":
                buffer = word
                prev_buffer = word
            else:
                buffer += sep + word

            if len(buffer) > width and first == False:
                if len(prev_buffer) > width and sep == ",":
                    text_list += Strutil.get_list(prev_buffer, " ")
                else:
                    text_list.append(prev_buffer)
                buffer = sep + word
            first = False

        if len(buffer) > width and sep == " ":
            #text_list += Strutil.get_list(buffer, " ")
            text_list.append(buffer[0:width-3] + "...")
        elif len(buffer) > width and sep == ",":
            text_list += Strutil.get_list(buffer, " ")
        else:
            text_list.append(buffer)

        return text_list
