#!/usr/bin/env python3
"""write text into a utf-8 file"""

def write_file(filename="", text=""):
    """write text into a file and return number of char written"""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
