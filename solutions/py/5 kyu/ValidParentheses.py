#!/usr/bin/python3

# https://www.codewars.com/kata/52774a314c2333f0a7000688/
def valid_parentheses(string):
    string = "".join(filter(lambda c: c in "()", string))
    while "()" in string:
        string = string.replace("()", "")
    return string == ""
