#!/usr/bin/python3

# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/
def solution(args):
    r = [[args[0]]]
    for i in args[1:]:
        if i == r[-1][-1] + 1:
            r[-1] += [i]
        else:
            r += [[i]]
    return ",".join(f"{a[0]}'-'{a[-1]}" if len(a) > 2 else ",".join(a) for a in r)
