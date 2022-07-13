#!/usr/bin/python3

# https://www.codewars.com/kata/55983863da40caa2c900004e/
def next_bigger(n):
    digits = [*map(int, str(n))]
    for i in range(1, len(digits)):
        if digits[-i] > digits[-(i + 1)]:
            prefix = digits[:-(i + 1)]
            postfix = digits[-i:]
            pivot = digits[-(i + 1)]
            postfix[postfix.index(m := min(filter(lambda x: x > pivot, postfix)))] = pivot
            return int("".join(map(str, prefix + [m] + sorted(postfix))))
    return -1
