#!/usr/bin/python3

# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/
def is_prime(p):
    if not p % 2:
        return False
    for i in range(3, int(pow(p, 0.5)) + 1):
        if not p % i:
            return False
    else:
        return True


def gap(g, m, n):
    cur = None
    for x in range(m, n + 1):
        if is_prime(x):
            last = cur
            cur = x
            if last:
                if cur - last == g:
                    return [last, cur]
