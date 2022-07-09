#!/usr/bin/python3

#https://www.codewars.com/kata/546f922b54af40e1e90001da/
from string import ascii_lowercase

def alphabet_position(text):
	return " ".join(str(ascii_lowercase.index(char) + 1) for char in text.lower() if char.isalpha())