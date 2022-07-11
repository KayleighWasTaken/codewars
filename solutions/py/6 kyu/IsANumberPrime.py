#!/usr/bin/python3

# https://www.codewars.com/kata/5262119038c0985a5b00029f/
def is_prime(num):
    if num < 2 or not num & 1 and num != 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if not num % i:
            return False
    return True
