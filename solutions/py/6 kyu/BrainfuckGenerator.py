#!/usr/bin/python3

# https://www.codewars.com/kata/579e646353ba33cce2000093/
def to_brainfuck(string):
    return "".join(f"{'+' * ord(c)}.>" for c in string)
