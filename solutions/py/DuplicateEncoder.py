#!/usr/bin/python3

# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/
def duplicate_encode(word):
    return "".join("(" if word.lower().count(char) == 1 else ")" for char in word.lower())
