#!/usr/bin/python3

# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/
def arithmetic(a, b, operator):
    match operator:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            return a / b
