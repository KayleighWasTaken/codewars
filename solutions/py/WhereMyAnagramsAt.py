#!/usr/bin/python3

#https://www.codewars.com/kata/523a86aa4230ebb5420001e1/
def anagrams(word, words):
	return [x for x in words if sorted(x) == sorted(word)]