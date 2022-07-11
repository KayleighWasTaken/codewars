#!/usr/bin/python3

# https://www.codewars.com/kata/53af2b8861023f1d88000832/
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0] in "rR" else f"{name} does not play banjo"