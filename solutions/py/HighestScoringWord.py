#!/usr/bin/python3

#https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/
from string import ascii_lowercase

def high(x):
	return max(x.split(" "), key = lambda word: sum((ascii_lowercase.index(char) + 1 for char in word)))