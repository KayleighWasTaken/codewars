#!/usr/bin/python3

# https://www.codewars.com/kata/550554fd08b86f84fe000a58/
def in_array(array1, array2):
    return sorted([s for s in set(array1) if any(s in s2 for s2 in array2)])
