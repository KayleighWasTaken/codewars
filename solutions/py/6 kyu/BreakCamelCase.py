#!/usr/bin/python3

# https://www.codewars.com/kata/5208f99aee097e6552000148/
def solution(s):
    return "".join(f" {c}" if 64 < ord(c) < 91 else c for c in s)
