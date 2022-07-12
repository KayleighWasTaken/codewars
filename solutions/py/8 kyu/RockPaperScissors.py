#!/usr/bin/python3

# https://www.codewars.com/kata/5672a98bdbdd995fad00000f/
def rps(p1, p2):
    return "Draw!" if p1 == p2 else "Player 1 won!" if ["paper", "rock", "scissors"][(len(p1) ^ 1) % 3] == p2 else "Player 2 won!"
