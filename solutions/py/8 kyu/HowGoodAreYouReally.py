#!/usr/bin/python3

# https://www.codewars.com/kata/5601409514fc93442500010b/
def better_than_average(class_points, your_points):
    return your_points > sum(class_points + [your_points]) / (len(class_points) + 1)
