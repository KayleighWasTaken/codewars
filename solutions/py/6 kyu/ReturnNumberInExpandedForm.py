#!/usr/bin/python3

# https://www.codewars.com/kata/5842df8ccbd22792a4000245/
def expanded_form(num):
    return " + ".join("0" * i + d for i, d in enumerate(str(num)[::-1]) if d != "0")[::-1]
