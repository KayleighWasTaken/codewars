#!/usr/bin/python3

# https://www.codewars.com/kata/54ba84be607a92aa900000f1/
def is_isogram(string):
    return sum(string.lower().count(char) for char in string.lower()) == len(string)
