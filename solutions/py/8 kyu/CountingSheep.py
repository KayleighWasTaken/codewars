#!/usr/bin/python3

# https://www.codewars.com/kata/54edbc7200b811e956000556/
def count_sheeps(sheep):
    return sum(1 for s in sheep if s)
