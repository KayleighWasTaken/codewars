#!/usr/bin/python3

# https://www.codewars.com/kata/5287e858c6b5a9678200083c/
def narcissistic( value ):
    return sum(pow(int(d), len(str(value))) for d in str(value)) == value
