#!/usr/bin/python3

# https://www.codewars.com/kata/54e6533c92449cc251001667/
def unique_in_order(iterable):
    return [x for i, x in enumerate(iterable) if iterable[i - 1] != x or not i]
