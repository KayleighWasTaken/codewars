#!/usr/bin/python3

# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/
def find_uniq(arr):
    return next(x for i, x in enumerate(arr) if (x != arr[i - 1]) & (x != arr[(i - 2)]))
