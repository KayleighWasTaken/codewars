#!/usr/bin/python3

# https://www.codewars.com/kata/5264d2b162488dc400000001/
def spin_words(sentence):
    return " ".join(word if len(word) < 5 else word[::-1] for word in sentence.split(" "))
