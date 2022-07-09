#!/usr/bin/python3

#https://www.codewars.com/kata/51c8e37cee245da6b40000bd/
def strip_comments(strng, markers):
	return "\n".join(line[:min([max(line.index(marker) - 1, 0) if marker in line else len(line) for marker in markers]) if len(markers) else len(line)].rstrip() for line in strng.split("\n"))