#!/usr/bin/python3

# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/
def wave(people):
    return [f"{people[:i]}{people[i:].capitalize()}" for i in range(len(people)) if people[i].isalpha()]
