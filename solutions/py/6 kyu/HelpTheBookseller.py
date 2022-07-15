#!/usr/bin/python3

# https://www.codewars.com/kata/54dc6f5a224c26032800005c/
def stock_list(listOfArt, listOfCat):
    return " - ".join(f"({cat} : {sum(int(art.split()[1]) for art in listOfArt if art[0] == cat)})" for cat in listOfCat) if listOfArt and listOfCat else ""
