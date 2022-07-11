#!/usr/bin/python3

# https://www.codewars.com/kata/555eded1ad94b00403000071/
def series_sum(n):
    return f"{sum(1 / (1 + 3 * i) for i in range(n)):0.2f}"
