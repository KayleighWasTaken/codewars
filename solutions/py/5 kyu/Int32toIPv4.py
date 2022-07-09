#!/usr/bin/python3

# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/
def int32_to_ip(int32):
    return f"{(int32 & 0xFF000000) >> 24}.{(int32 & 0xFF0000) >> 16}.{(int32 & 0xFF00) >> 8}.{int32 & 0xFF}"
