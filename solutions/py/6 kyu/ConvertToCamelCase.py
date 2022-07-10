#!/usr/bin/python3

# https://www.codewars.com/kata/517abf86da9663f1d2000003/
def to_camel_case(text):
    return "".join(word.capitalize() if i or word[0].isupper() else word.lower() for i, word in enumerate(text.translate(str.maketrans({'_': ' ', '-': ' '})).split()))
