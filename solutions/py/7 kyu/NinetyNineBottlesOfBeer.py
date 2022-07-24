#!/usr/bin/python3

# https://www.codewars.com/kata/52a723508a4d96c6c90005ba/
def sing():
    lyrics = []
    for i in range(99):
        lyrics += [f"{99 - i} bottle{'s' if i != 98 else ''} of beer on the wall, {99 - i} bottle{'s' if i != 98 else ''} of beer."]
        lyrics += [f"Take one down and pass it around, {98 - i if i != 98 else 'no more'} bottle{'s' if i != 97 else ''} of beer on the wall."]
    lyrics += ["No more bottles of beer on the wall, no more bottles of beer."]
    lyrics += ["Go to the store and buy some more, 99 bottles of beer on the wall."]
    return lyrics
