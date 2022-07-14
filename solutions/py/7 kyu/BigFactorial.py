#!/usr/bin/python3

# https://www.codewars.com/kata/54f0d5447872e8ce9f00013d/
def factorial(n):
    f = 1
    return [f := f * x for x in range(1, n + 1)][-1] if n > 0 else 1 if n == 0 else None
