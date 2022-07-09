#!/usr/bin/python3

# https://www.codewars.com/kata/52685f7382004e774f0001f7/
def make_readable(seconds):
    return f"{str(seconds // 3600).zfill(2)}:{str(seconds // 60 % 60).zfill(2)}:{str(seconds % 60).zfill(2)}"
