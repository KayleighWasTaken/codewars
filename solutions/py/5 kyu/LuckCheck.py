#!/usr/bin/python3

# https://www.codewars.com/kata/5314b3c6bb244a48ab00076c/
def luck_check(string):
    return sum(map(int, string[(i := -len(string) // 2):])) == sum(map(int, string[:-i]))
