#!/usr/bin/python3

# https://www.codewars.com/kata/586dd26a69b6fd46dd0000c0/
def my_first_interpreter(code):
    memory_cell = 0
    output = ""
    for instruction in code:
        match instruction:
            case "+":
                memory_cell = (memory_cell + 1) & 0xFF
            case ".":
                output = output + chr(memory_cell)
            case _:
                pass
    return output
