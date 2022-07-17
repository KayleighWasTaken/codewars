#!/usr/bin/python3

# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/
def is_palindrome(s):
    return (l := s.lower()) == l[::-1]
