#!/usr/bin/env python3


# if len(sys.argv) > 2:
#     print(f"Name file: {sys.argv[0]}\n", f"First argv: {sys.argv[1]}\n", f"Second argv: {sys.argv[2]}\n")
# else:
#     print("No argv")
import sys


if len(sys.argv) > 1:
    a = sys.argv[1:]
    ab = {}
    k = False
    for i in a:
        if "=" in i:
            c = i.split("=")
            ab[c[0]] = c[1]
        if i == "--sort":
            k = True
    if k:
        d = dict(sorted(ab.items()))
        for i, e in d.items():
            print(f"Key: {i} Value: {e}")
    else:
        for i, e in ab.items():
            print(f"Key: {i} Value: {e}")
