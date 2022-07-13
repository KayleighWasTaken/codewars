#!/usr/bin/python3

# https://www.codewars.com/kata/52c31f8e6605bcc646000082/
def two_sum(numbers, target):
    for i in (r := [*range(len(numbers))]):
        for j in r[i + 1:]:
            if numbers[i] + numbers[j] == target:
                return [i, j]
