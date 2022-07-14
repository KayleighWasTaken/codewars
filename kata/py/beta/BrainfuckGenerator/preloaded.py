#!/usr/bin/python3

def brainfuck_interpreter(program):
    program_counter = 0
    tape_index = 0
    tape = [0] * 30000
    return_stack = []
    output = ""

    while program_counter < len(program):
        match program[program_counter]:
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
                raise NotImplementedError("Input isn't implemented, I'm not making it that easy :^)")
            case "[":
                if tape[tape_index] != 0:
                    return_stack.append(program_counter)
                    program_counter += 1
                else:
                    bracket_count = 1
                    while bracket_count:
                        program_counter += 1
                        if program[program_counter] == "[":
                            bracket_count += 1
                        elif program[program_counter] == "]":
                            bracket_count -= 1
                    program_counter += 1
            case "]":
                program_counter = return_stack.pop()
    return output


print(brainfuck_interpreter("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."))

