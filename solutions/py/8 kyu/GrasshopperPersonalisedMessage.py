#!/usr/bin/python3

# https://www.codewars.com/kata/5772da22b89313a4d50012f7/
def greet(name, owner):
    return f"Hello {['guest', 'boss'][name == owner]}"
