#!/usr/bin/python3

# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/
def first_non_consecutive(arr):
    return next((i + 1 for i in range(min(arr), max(arr)) if i not in arr), False)
