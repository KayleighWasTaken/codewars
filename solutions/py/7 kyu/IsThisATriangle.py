#!/usr/bin/python3

# https://www.codewars.com/kata/56606694ec01347ce800001b/
def is_triangle(a, b, c):
    return max(a, b, c) < a + b + c - max(a, b, c)
