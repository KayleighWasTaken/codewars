#!/usr/bin/python3

# https://www.codewars.com/kata/57f609022f4d534f05000024/
def stray(arr):
    return next(x for x in arr if arr.count(x) == 1)
