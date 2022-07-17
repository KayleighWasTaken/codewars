#!/usr/bin/python3

# https://www.codewars.com/kata/52c4dd683bfd3b434c000292/
def is_interesting(number, awesome_phrases):
    for i in range(3):
        if (num_str_len := len(num_str := str(number + i))) > 2:
            if number + i in awesome_phrases:
                return 1 if i else 2
            if not (number + i) % (10 ** (num_str_len - 1)):
                return 1 if i else 2
            if len(set(num_str)) == 1:
                return 1 if i else 2
            if all([*range(1, 10), 0].index(int(x)) - [*range(1, 10), 0].index(int(num_str[p + 1])) == -1 for p, x in enumerate(num_str[:-1])):
                return 1 if i else 2
            if all([*range(9, -1, -1)].index(int(x)) - [*range(9, -1, -1)].index(int(num_str[p + 1])) == -1 for p, x in enumerate(num_str[:-1])):
                return 1 if i else 2
            if num_str[:num_str_len // 2][::-1] == num_str[-(num_str_len // 2):]:
                return 1 if i else 2
    return 0
