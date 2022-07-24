#!/usr/bin/python3

# https://www.codewars.com/kata/564057bc348c7200bd0000ff/
def thirt(n):
    return n if n == (res := sum(int(c) * [1, 10, 9, 12, 3, 4][i % 6] for i, c in enumerate(str(n)[::-1]))) else thirt(res)
