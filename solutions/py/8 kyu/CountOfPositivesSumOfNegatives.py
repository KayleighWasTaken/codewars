#!/usr/bin/python3

# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/
def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0]), sum(x for x in arr if x < 0)] if arr else []
