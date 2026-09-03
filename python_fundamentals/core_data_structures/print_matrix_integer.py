#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:
            print()
            continue
        line = ""
        for i, val in enumerate(row):
            line += "{:d}".format(val)
            if i < len(row) - 1:
                line += " "
        print(line)
