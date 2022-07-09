#!/usr/bin/python3

# https://www.codewars.com/kata/54da5a58ea159efa38000836/
def find_it(seq):
    a = 0
    return [a := a ^ x for x in seq][-1]
