#!/usr/bin/python3

#https://www.codewars.com/kata/526571aae218b8ee490006f4/
def count_bits(n):
	return len([bit for bit in bin(n) if bit == "1"])