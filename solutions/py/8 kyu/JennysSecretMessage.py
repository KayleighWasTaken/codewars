#!/usr/bin/python3

# https://www.codewars.com/kata/55225023e1be1ec8bc000390/
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
