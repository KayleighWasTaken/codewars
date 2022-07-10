#!/usr/bin/python3

def possibilities(param):
    return [param.replace("?", "{}").format(*n) for n in [f"{bin(x)[2:].zfill(param.count('?'))}" for x in range(2 ** param.count("?"))]]
