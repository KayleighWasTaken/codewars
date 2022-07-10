#!/usr/bin/python3

# https://www.codewars.com/kata/52597aa56021e91c93000cb0/
def move_zeros(lst):
    return [x for x in lst if x] + [0] * lst.count(0)
