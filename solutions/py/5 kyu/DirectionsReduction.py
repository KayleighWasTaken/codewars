#!/usr/bin/python3

# https://www.codewars.com/kata/550f22f4d758534c1100025a/
def dirReduc(arr):
    path = []
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    for d in arr:
        if path and path[-1] == opposites[d]:
            path.pop()
        else:
            path.append(d)
    return path
