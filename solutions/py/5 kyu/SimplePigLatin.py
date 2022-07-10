#!/usr/bin/python3

# https://www.codewars.com/kata/520b9d2ad5c005041100000f/
def pig_it(text):
    return " ".join(f"{word[1:] + word[0]}ay" if word[0].isalpha() else word for word in text.split())
