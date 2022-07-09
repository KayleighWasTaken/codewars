#!/usr/bin/python3

# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/
def valid_braces(string):
    stack = []
    for brace in string:
        match brace:
            case "(":
                stack.append(")")
            case "[":
                stack.append("]")
            case "{":
                stack.append("}")
            case _:
                if len(stack):
                    if stack.pop() != brace:
                        return False
    return len(stack) == 0
