#!/usr/bin/python3

# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/
def digitize(n):
    return [int(d) for d in str(n)[::-1]]
