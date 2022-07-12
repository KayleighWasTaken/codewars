#!/usr/bin/python3

# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/
def number(lines):
    return [f"{i + 1}: {s}" for i, s in enumerate(lines)]
