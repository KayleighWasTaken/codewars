#!/usr/bin/python3

# https://www.codewars.com/kata/570409d3d80ec699af001bf9/
def fusc(n):
    return n if n < 2 else fusc(n // 2) + fusc(n // 2 + 1) if n & 1 else fusc(n // 2)
