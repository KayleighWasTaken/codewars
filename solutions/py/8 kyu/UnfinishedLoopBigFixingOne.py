#!/usr/bin/python3

# https://www.codewars.com/kata/55c28f7304e3eaebef0000da/
def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res
