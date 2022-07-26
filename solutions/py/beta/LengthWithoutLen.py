#!/usr/bin/python3

# https://www.codewars.com/kata/62c8d290cef6f10057dfa0ca/
def length_without_len(string):
    return string.rfind(string[-1]) + 1 if string else 0
