#!/usr/bin/python3

# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/
def zeros(n):
    z = 0
    while n >= 5:
        n //= 5
        z += n
    return z
