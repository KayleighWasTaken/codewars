#!/usr/bin/python3

# https://www.codewars.com/kata/523b4ff7adca849afe000035/
def greet():
    return "".join(chr((10334410032606748633331426664 >> i * 8) % 256) for i in range(12))
