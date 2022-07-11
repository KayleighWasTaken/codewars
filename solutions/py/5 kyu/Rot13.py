#!/usr/bin/python3

# https://www.codewars.com/kata/530e15517bc88ac656000716/
def rot13(message):
    return "".join(chr(97 + ((o - 84) % 26)) if 123 > o > 96 else chr(65 + ((o - 52) % 26)) if 91 > o > 64 else chr(o) for o in map(ord, message))
