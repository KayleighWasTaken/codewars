#!/usr/bin/python3

# https://www.codewars.com/kata/54ff3102c1bad923760001f3/
def get_count(sentence):
    return sum([sentence.count(v) for v in ["a", "e", "i", "o", "u"]])
