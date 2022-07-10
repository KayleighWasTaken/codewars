#!/usr/bin/python3

# https://www.codewars.com/kata/54b724efac3d5402db00065e/
def decode_morse(morse_code):
    return " ".join("".join(MORSE_CODE[c] if c != "" else " " for c in morse_code.split(" ")).split())
