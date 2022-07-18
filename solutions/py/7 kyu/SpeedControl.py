#!/usr/bin/python3

# https://www.codewars.com/kata/56484848ba95170a8000004d/
def gps(s, x):
    return 3600 * max(*[x[i + 1] - d for i, d in enumerate(x[:-1])]) / s if len(x) > 1 else 0
