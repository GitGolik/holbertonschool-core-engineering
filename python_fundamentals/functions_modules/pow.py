#!/usr/bin/env python3

def pow(a, b):
    if b == 0:
        result = 1

    for compt in range(b):
        result = result * a

    return result
