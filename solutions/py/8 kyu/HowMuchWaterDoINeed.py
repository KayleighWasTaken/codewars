#!/usr/bin/python3

# https://www.codewars.com/kata/575fa9afee048b293e000287/ (btw the single worst kata on codewars)
def how_much_water(water, load, clothes):
    if clothes > 2 * load:
        return "Too much clothes"
    elif clothes < load:
        return "Not enough clothes"
    else:
        return round(water * 1.1 ** (clothes - load), 2)
