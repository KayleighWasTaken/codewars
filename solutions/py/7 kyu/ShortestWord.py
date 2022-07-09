#!/usr/bin/python3

# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/
def find_short(s):
    return len(min(s.split(" "), key=lambda x: len(x)))
