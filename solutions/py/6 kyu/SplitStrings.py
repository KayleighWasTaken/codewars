#!/usr/bin/python3

# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/
def solution(s):
    return list(filter(None, [s[x:x + 2] for x in range(0, len(s) - 1, 2)] + [f"{s[-1]}_" if len(s) & 1 else None]))
