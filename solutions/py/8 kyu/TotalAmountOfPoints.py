#!/usr/bin/python3

# https://www.codewars.com/kata/5bb904724c47249b10000131/
def points(games):
    return sum(3 if s[0] > s[2] else s[0] == s[2] for s in games)