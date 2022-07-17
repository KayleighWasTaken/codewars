#!/usr/bin/python3

# https://www.codewars.com/kata/62d1eb93e5994c003156b2ae/
def encode(string):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    return " ".join(f"{'.' * (letters.index(c) % 3 + 1)} {'.' * ((letters.index(c) // 3) % 3 + 1)} {'.' * (letters.index(c) // 9 + 1)}" for c in string)


def decode(string):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    dots = string.split()
    output = ""
    for i in range(len(dots) // 3):
        col, row, layer = dots[i * 3:i * 3 + 3]
        output = output + letters[(len(col) - 1) + ((len(row) - 1) * 3) + ((len(layer) - 1) * 9)]
    return output
