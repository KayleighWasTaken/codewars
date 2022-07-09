#!/usr/bin/python3

# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/
def likes(names):
    return f"{('no one' if not len(names) else names[0])}{'' if len(names) < 2 else f' and {names[1]}' if len(names) == 2 else f', {names[1]} and {names[2]}' if len(names) == 3 else f', {names[1]} and {len(names) - 2} others'} {'likes' if len(names) <=1 else 'like'} this"
