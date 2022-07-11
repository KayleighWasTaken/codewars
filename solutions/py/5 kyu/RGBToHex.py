#!/usr/bin/python3

# https://www.codewars.com/kata/513e08acc600c94f01000001/
def rgb(r, g, b):
    return "".join(f"{min(max(v, 0), 255):0{2}X}" for v in [r, g, b])
