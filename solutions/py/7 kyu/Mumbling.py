#!/usr/bin/python3

# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/
def accum(s):
    return "-".join(f"{c.upper() + (c * i)}" for i, c in enumerate(s.lower()))
