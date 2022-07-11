#!/usr/bin/python3

# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/
def count_sheep(n):
    return "".join(f"{i + 1} sheep..." for i in range(n))
