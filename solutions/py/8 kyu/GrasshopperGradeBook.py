#!/usr/bin/python3

# https://www.codewars.com/kata/55cbd4ba903825f7970000f5/
def get_grade(s1, s2, s3):
    match s := sum((s1, s2, s3)) // 3:
        case _ if s < 60:
            return "F"
        case _ if s < 70:
            return "D"
        case _ if s < 80:
            return "C"
        case _ if s < 90:
            return "B"
        case _:
            return "A"
