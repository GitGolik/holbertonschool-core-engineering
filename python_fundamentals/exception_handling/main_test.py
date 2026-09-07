#!/usr/bin/env python3


safe_print_integer = __import__('safe_print_integer').safe_print_integer

value = 2

valueTorF = safe_print_integer(value)
print(f"{valueTorF}")
