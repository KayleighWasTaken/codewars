#!/usr/bin/python3

# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/
def human_years_cat_years_dog_years(human_years):
    return [human_years,15 + (9 * (human_years > 1) + (max((human_years - 2), 0) * 4)), 15 + (9 * (human_years > 1)) + (max((human_years - 2), 0) * 5)]
