#!/usr/bin/python3

# https://www.codewars.com/kata/58bb39ab39fdb4c4370005ac/
def enchant(dust, feather, essence):
    if dust >= 8 and feather >= 5 and essence >= 2:
        return 1 + enchant(dust - 8, feather - 5, essence - 2)
    elif dust >= 4 and feather >= 3 and essence >= 1:
        return 1 + enchant(dust - 4, feather - 3, essence - 1)
    elif dust >= 2 and feather >= 1 and essence >= 1:
        return 1 + enchant(dust - 2, feather - 1, essence - 1)
    else:
        return 0
