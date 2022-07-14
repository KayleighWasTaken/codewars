#!/usr/bin/python3

# https://www.codewars.com/kata/526156943dfe7ce06200063e/
def brain_luck(code, program_input):
    program_counter = 0
    tape_index = 0
    tape = [0] * 30000
    return_stack = []
    output = ""

    while program_counter < len(code):
        match code[program_counter]:
            case ">":
                tape_index += 1
                program_counter += 1
            case "<":
                tape_index -= 1
                program_counter += 1
            case "+":
                tape[tape_index] = (tape[tape_index] + 1) & 0xFF
                program_counter += 1
            case "-":
                tape[tape_index] = (tape[tape_index] - 1) & 0xFF
                program_counter += 1
            case ".":
                output = output + chr(tape[tape_index])
                program_counter += 1
            case ",":
                print(program_input)
                tape[tape_index] = program_input[0]
                program_input = program_input[1:]
            case "[":
                if tape[tape_index] != 0:
                    return_stack.append(program_counter)
                    program_counter += 1
                else:
                    bracket_count = 1
                    while bracket_count:
                        program_counter += 1
                        if code[program_counter] == "[":
                            bracket_count += 1
                        elif code[program_counter] == "]":
                            bracket_count -= 1
                    program_counter += 1
            case "]":
                program_counter = return_stack.pop()
    return output
