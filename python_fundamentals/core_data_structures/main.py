#!/usr/bin/env python3

element_at = __import__('element_at').element_at

my_list = ["a", "b", "c", "d", "e"]
print(element_at(my_list, 3))
print(element_at(my_list, 0))
print(element_at(my_list, 4))
print(element_at(my_list, 5))
print(element_at(my_list, -14))
print(element_at(my_list, 32))
print(element_at(my_list, 15))
