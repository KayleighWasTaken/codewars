#!/usr/bin/python3

# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/
def find_missing_letter(chars):
    return chr(next(ord(c) + 1 for i, c in enumerate(chars) if ord(chars[i + 1]) - ord(c) == 2))
