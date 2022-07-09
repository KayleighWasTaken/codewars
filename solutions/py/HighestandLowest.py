#!/usr/bin/python3

#https://www.codewars.com/kata/554b4ac871d6813a03000035
def high_and_low(numbers):
    return "{} {}".format(max([int(x) for x in numbers.split(" ")]), min([int(x) for x in numbers.split(" ")])) # horrifying but its a oneliner
