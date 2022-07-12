#!/usr/bin/python3

# https://www.codewars.com/kata/568d0dd208ee69389d000016/
def rental_car_cost(d):
    return d * 40 - (20 * (d >= 3)) - (30 * (d >= 7))