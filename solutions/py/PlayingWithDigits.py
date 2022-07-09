#!/usr/bin/python3

#https://www.codewars.com/kata/5552101f47fc5178b1000050/
def dig_pow(n, p):
	x = sum(pow(int(d), p + i) for i, d in enumerate(str(n)))
	return x // n if x % n == 0 else -1