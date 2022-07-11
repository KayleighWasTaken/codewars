#!/usr/bin/python3

# https://www.codewars.com/kata/550498447451fbbd7600041c/
def comp(array1, array2):
    return all([sorted(array2)[i] == x * x for i, x in enumerate(sorted(array1, key=abs))]) if None not in (array1, array2) and len(array1) == len(array2) else False
