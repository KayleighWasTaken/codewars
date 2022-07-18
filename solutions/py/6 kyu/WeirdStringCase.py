#!/usr/bin/python3

# https://www.codewars.com/kata/52b757663a95b11b3d00062d/
def to_weird_case(string):
    return " ".join("".join(c.lower() if i % 2 else c.upper() for i, c in enumerate(w)) for w in string.split())
