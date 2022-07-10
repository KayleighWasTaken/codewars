#!/usr/bin/python3

# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/
def sort_array(source_array):
    f = (x for x in sorted(source_array) if x & 1)
    return[next(f) if x & 1 else x for x in source_array]
