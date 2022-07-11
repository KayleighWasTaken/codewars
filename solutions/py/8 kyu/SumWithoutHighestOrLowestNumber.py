#!/usr/bin/python3

# https://www.codewars.com/kata/576b93db1129fcf2200001e6/
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0
