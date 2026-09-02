#!/usr/bin/env python3

def print_last_digit(number):

    if number < 0:
    result = abs(number) % 10

    print(result, end="")
    return result
