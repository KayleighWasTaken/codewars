#!/usr/bin/python3

# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/
def number(bus_stops):
    return sum(on - off for on, off in bus_stops)
