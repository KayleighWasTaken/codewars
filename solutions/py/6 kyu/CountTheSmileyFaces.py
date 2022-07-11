#!/usr/bin/python3

# https://www.codewars.com/kata/583203e6eb35d7980400002a/
def count_smileys(arr):
    return len([s for s in filter(lambda x: x[0] in ";:" and (x[1] in "-~" and x[2] in ")D" if len(x) == 3 else x[1] in ")D"), arr)])
