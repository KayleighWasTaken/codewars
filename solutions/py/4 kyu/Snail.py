#!/usr/bin/python3

# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/
def snail(snail_map):
    if snail_map == [[]]:
        return []

    snail_path = []

    x = -1
    y = 0
    segment = 0

    for length in [len(snail_map) - (i // 2) for i in range(1, (len(snail_map) * 2))]:
        for _ in range(length):
            match segment % 4:
                case 0:
                    x += 1
                case 1:
                    y += 1
                case 2:
                    x -= 1
                case 3:
                    y -= 1
            snail_path.append(snail_map[y][x])
        segment += 1

    return snail_path
