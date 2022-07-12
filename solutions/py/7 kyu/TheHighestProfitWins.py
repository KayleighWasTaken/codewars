#!/usr/bin/python3

# https://www.codewars.com/kata/559590633066759614000063/
def min_max(lst):
    return sorted(lst)[::len(lst) - 1]
