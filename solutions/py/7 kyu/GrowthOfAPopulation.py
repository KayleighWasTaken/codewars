#!/usr/bin/python3

# https://www.codewars.com/kata/563b662a59afc2b5120000c6/
def nb_year(p0, percent, aug, p, years = 0):
    return years if p0 >= p else nb_year(int(p0 + (p0 * percent / 100) + aug), percent, aug, p, years + 1)
