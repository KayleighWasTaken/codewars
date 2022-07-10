#!/usr/bin/python3

# https://www.codewars.com/kata/56541980fa08ab47a0000040/
def printer_error(s):
    return f"{sum(s.count(x) for x in set(s) if x > 'm')}/{len(s)}"
