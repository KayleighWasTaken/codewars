#!/usr/bin/python3

# https://www.codewars.com/kata/5694d22eb15d78fe8d00003a/
def group_in_10s(*args):
    a = [[] for i in range((max(args) // 10 + 1))] if args else []
    for n in sorted(args):
        i = n // 10
        a[i].append(n)
    a = [x if x else None for x in a]
    return a
