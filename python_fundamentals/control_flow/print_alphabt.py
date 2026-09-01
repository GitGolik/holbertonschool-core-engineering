#!/usr/bin/env python3

alphabet = "".join(chr(c) for c in range(ord('a'), ord ('z') + 1) if chr(c) not in ('q', 'e'))
print("{}".format(alphabet))
