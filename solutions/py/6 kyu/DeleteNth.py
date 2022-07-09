#!/usr/bin/python3

# https://www.codewars.com/kata/554ca54ffa7d91b236000023/
def delete_nth(order, max_e):
    return [order[i] for i in range(len(order)) if order[:i].count(order[i]) < max_e]
