#!/usr/bin/env python3
"""append text into a file"""


def append_write(filename="", text=""):
    """append text into a file and return number of char added"""

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
