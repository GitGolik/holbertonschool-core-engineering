#!/usr/bin/env python3
"""read and print text file"""


def read_file(filename=""):
    """read text file and print in stdout"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
