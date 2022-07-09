#!/usr/bin/python3

# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/
def tower_builder(n_floors):
    return [(" " * (n_floors - i)) + ("*" * (i * 2 - 1)) + (" " * (n_floors - i)) for i in range(1, n_floors + 1)]
