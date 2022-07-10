#!/usr/bin/python3

# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/
def duplicate_count(text):
    return len([char for char in set(text.lower()) if text.lower().count(char) > 1])
