#!/usr/bin/python3

# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/
def solution(string, ending):
    return string[-len(ending):] == ending or not ending
