#!/usr/bin/python3

# https://www.codewars.com/kata/588f3e0dfa74475a2600002a/
def possibilities(param):  # no imports, no recursion, no newlines, only gaming :sunglasses:
    return [param.replace("?", "{}").format(*n) for n in [f"{bin(x)[2:].zfill(param.count('?'))}" for x in range(2 ** param.count("?"))]]
