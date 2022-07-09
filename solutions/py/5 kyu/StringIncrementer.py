#!/usr/bin/python3

# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/
def increment_string(strng):
    num = "".join(char for pos, char in enumerate(strng) if strng[pos:].isdigit())
    return strng.rstrip(num) + (str((int(num) + 1)).rjust(len(num), "0") if num != "" else "1")
