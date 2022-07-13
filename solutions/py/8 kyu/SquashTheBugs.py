#!/usr/bin/python3

# https://www.codewars.com/kata/56f173a35b91399a05000cb7/
def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i = 0
    while i <= len(spl):
        if len(spl[i]) > longest:
            longest = len(spl[i])
        i += 1
    return longest
