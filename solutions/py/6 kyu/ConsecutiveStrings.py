#!/usr/bin/python3

# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/
def longest_consec(strarr, k):
    return sorted(["".join(strarr[i:i + k]) for i in range(len(strarr) - (k - 1))], key=lambda s: -len(s))[0] if len(strarr) >= k > 0 else ""
