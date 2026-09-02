#!/usr/bin/env python3

def pow(a, b):

    for compt in range(b):
        if b == 0:
            result = 1
        else:
            result = result * a

    return result
