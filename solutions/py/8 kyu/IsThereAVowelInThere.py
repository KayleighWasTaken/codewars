#!/usr/bin/python3

# https://www.codewars.com/kata/57cff961eca260b71900008f/
def is_vow(inp):
    return [c if (c := chr(x)) in "aeiou" else x for x in inp]
