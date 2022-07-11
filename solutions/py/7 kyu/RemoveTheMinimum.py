#!/usr/bin/python3

# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/
def remove_smallest(numbers):
    return [n for i, n in enumerate(numbers) if n != min(numbers) or i != numbers.index(n)]
