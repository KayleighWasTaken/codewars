#!/usr/bin/python3

# https://www.codewars.com/kata/52449b062fb80683ec000024/
def generate_hashtag(s):
    return r if 1 < len(r := "#" + "".join(w for w in s.title().split())) <= 140 else (r := False)
