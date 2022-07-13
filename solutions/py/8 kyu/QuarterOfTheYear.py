#!/usr/bin/python3

# https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/
def quarter_of(month):
    return month // 3 + bool(month % 3)

def quarter_of(month):
    return (month + 2) // 3
