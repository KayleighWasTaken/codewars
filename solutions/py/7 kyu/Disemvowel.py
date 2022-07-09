#!/usr/bin/python3

# https://www.codewars.com/kata/52fba66badcd10859f00097e/
def disemvowel(string_):
    return "".join(c for c in string_ if c not in "aeiouAEIOU")