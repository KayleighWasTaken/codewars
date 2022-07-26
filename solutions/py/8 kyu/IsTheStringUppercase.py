#!/usr/bin/python3

# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/
def is_uppercase(inp):
    return all(map(lambda x: x.isupper() or not x.isalpha(), inp))
