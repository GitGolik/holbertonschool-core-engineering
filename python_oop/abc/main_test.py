#!/usr/bin/env python3
from verboselist import VerboseList

v1 = VerboseList([1, 2, 3])
v1.append(4)
v1.extend([5, 6])
v1.remove(2)
v1.pop()
v1.pop(0)
