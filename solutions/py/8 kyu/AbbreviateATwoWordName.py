#!/usr/bin/python3

# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
def abbrev_name(name):
    return f"{name[0]}.{name.split()[1][0]}".upper()
