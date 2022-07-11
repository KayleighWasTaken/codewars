#!/usr/bin/python3

# https://www.codewars.com/kata/54f9c37106098647f400080a/
def drop_while(arr, pred):
    return [arr[i + 1:] for i in range(len(arr)) if all(map(pred, arr[:i + 1]))][-1]


