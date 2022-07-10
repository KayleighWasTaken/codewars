#!/usr/bin/python3

# https://www.codewars.com/kata/54da539698b8a2ad76000228/
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")
