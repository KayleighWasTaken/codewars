#!/usr/bin/python3

# https://www.codewars.com/kata/514b92a657cdc65150000006/
def solution(number):
    return sum([x for x in range(number) if (x % 3 == 0) | (x % 5 == 0)])
