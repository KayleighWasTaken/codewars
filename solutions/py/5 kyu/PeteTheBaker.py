#!/usr/bin/python3

# https://www.codewars.com/kata/525c65e51bf619685c000059/
def cakes(recipe, available):
    return min(available[ingredient] // recipe[ingredient] if ingredient in available else 0 for ingredient in recipe.keys())
