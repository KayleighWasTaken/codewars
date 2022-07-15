#!/usr/bin/python3

# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/
def scramble(s1, s2):
    return set(s1) >= set(s2) and all(s1.count(c) >= s2.count(c) for c in set(s2))
