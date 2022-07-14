#!/usr/bin/python3

# https://www.codewars.com/kata/56968ce7753513604b000055/
def pyramid_height(n):
    return int(round(1/2 * (-1 + (108 * n + (-3 + 11664 * n ** 2) ** 0.5) ** (1/3) / 3 ** (2 / 3) + 1 / (324 * n + 3 * (-3 + 11664 * n ** 2) ** 0.5) ** (1/3)), 3))
