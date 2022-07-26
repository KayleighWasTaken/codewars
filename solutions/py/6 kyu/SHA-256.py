#!/usr/bin/python3

# https://www.codewars.com/kata/587fb57e12fc6eadf200009b/
from hashlib import sha256


def to_sha256(s):
    return sha256(str.encode(s)).hexdigest()
