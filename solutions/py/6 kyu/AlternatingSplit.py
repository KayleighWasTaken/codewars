#!/usr/bin/python3

# https://www.codewars.com/kata/57814d79a56c88e3e0000786/
def decrypt(encrypted_text, n):
    if not encrypted_text:
        return encrypted_text
    else:
        encrypted_text = [*encrypted_text]
    for i in range(n):
        encrypted_text[1::2], encrypted_text[::2] = encrypted_text[:len(encrypted_text) // 2], encrypted_text[len(encrypted_text) // 2:]
    return "".join(encrypted_text)


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
