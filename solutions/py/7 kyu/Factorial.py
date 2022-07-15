#!/usr/bin/python3

# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/
def factorial(n):
    if not 0 <= n <= 12:
        raise ValueError
    else:
        f = 1
        for i in range(n):
            f *= i + 1
        return f
