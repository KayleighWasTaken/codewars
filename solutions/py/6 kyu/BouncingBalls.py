#!/usr/bin/python3

# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/
def bouncing_ball(h, bounce, window):
    if h > window > 0 and 1 > bounce > 0:
        observations = -1
        while h > window:
            h *= bounce
            observations += 2
        return observations
    else:
        return -1
