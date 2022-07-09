#!/usr/bin/python3

# https://www.codewars.com/kata/546e2562b03326a88e000020/
def square_digits(num):
    return int("".join(str(int(x) ** 2) for x in str(num)))
