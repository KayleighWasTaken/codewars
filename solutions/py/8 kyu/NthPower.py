#!/usr/bin/python3

# https://www.codewars.com/kata/57d814e4950d8489720008db/
def index(array, n):
    return array[n] ** n if n < len(array) else -1
