#!/usr/bin/env python3

def safe_print_division(a, b):
    i = None
    try:
        i = a / b
    except Exception:
        print("Inside result: None")
    finally:
        if i is not None:
            print("Inside result: {}".format(i))
    return i
