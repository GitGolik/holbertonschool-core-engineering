#!/usr/bin/env python3

def uppercase(str):
    for character in str:
        code = ord(character)

        if ord('a') <= code <= ord('z'):
            character = chr(code - 32)

        print(character, end="")

    print()
