#!/usr/bin/python3

# https://www.codewars.com/kata/529bf0e9bdf7657179000008/
def valid_solution(board):
    # turn board into a 1d list
    one_d_board = sum(board, [])
    # check for missing digits
    if sum(one_d_board) != 405:
        return False
    # rows are made up of nine consecutive elements, eg: row 3 is indices 27 through 35
    row = lambda i, b: b[i * 9: (i + 1) * 9]
    # columns are made up of every ninth element, eg: column 0 is indices 0 9 18 27 36 45 54 63 72
    col = lambda i, b: b[i::9]
    # boxes are three sets of three consecutive elements spaced by nine, eg: box 4 is indices 27 28 29 36 37 38 45 46 47
    box = lambda i, b: sum((b[i * 3 + (i // 3 * 18) + x:i * 3 + (i // 3 * 18) + x + 21:9] for x in range(3)), [])
    # check all rows, cols, and boxes are valid
    for i in range(9):
        if len(set(row(i, one_d_board))) == len(set(col(i, one_d_board))) == len(set(box(i, one_d_board))) == 9:
            pass
        else:
            return False

    return True
