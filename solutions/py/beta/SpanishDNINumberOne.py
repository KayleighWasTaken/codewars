#!/usr/bin/python3

# https://www.codewars.com/kata/609f9a49d5a5fc000790db58/
def dni_solver(dni):
    return dni[:-1] + 'TRWAGMYFPDXBNJZSQVHLCKE'[int(dni[:-1]) % 23]
