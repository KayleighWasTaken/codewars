#!/usr/bin/python3

# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3/
def find_uniq(arr):
    sets = [set(s.lower().replace(" ", "")) for s in arr]
    return next(arr[i] for i, s in enumerate(sets) if (s != sets[i - 1]) & (s != sets[(i - 2)]))
