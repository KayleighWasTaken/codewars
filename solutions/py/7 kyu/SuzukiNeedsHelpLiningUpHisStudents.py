#!/usr/bin/python3

# https://www.codewars.com/kata/5701800886306a876a001031/
def lineup_students(string):
    return sorted(sorted(string.split(), reverse=True), key=len, reverse=True)
