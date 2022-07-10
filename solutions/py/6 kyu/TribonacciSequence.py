#!/usr/bin/python3

# https://www.codewars.com/kata/556deca17c58da83c00002db/
def tribonacci(signature, n):
    return signature[:n] if n <= len(signature) else tribonacci(signature + [sum(signature[-3:])], n)
