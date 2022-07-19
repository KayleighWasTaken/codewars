#!/usr/bin/python3

# https://www.codewars.com/kata/5286b2e162056fd0cb000c20/
def collatz(n):
    path = []
    while n != 1:
        path.append(str(n))
        n = n * 3 + 1 if n & 1 else n // 2
    return "->".join(path)
