#!/usr/bin/python3

# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/
def first_non_repeating_letter(string):
    return next((c for c in string if string.lower().count(c.lower()) == 1), "")
