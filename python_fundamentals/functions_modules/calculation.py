#!/usr/bin/env python3

from calculator_1 import addition
from calculator_1 import subtraction
from calculator_1 import multiplication
from calculator_1 import division

a = 10
b = 5

if __name__ == "__main__":
    print("{}".format(addition(a, b)))
    print("{}".format(subtraction(a, b)))
    print("{}".format(multiplication(a, b)))
    print("{}".format(division(a, b)))
