#!/usr/bin/python3

# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/
def max_sequence(arr):
    return max([sum(arr[i:i + l]) for l in range(len(arr)) for i in range(len(arr) - l)] + [0])
