#!/usr/bin/python3

# https://www.codewars.com/kata/62cecd4e5487c10028996e04/
def race_podium(blocks):
    return (s := ((blocks + 2) // 3), s + 1, blocks - (2 * s + 1)) if blocks != 7 else (2, 4, 1)
