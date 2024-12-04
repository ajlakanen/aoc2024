import re

file = open("data/04.txt", "r")
content = file.read()
lines = content.split("\n")


def findMAS(i, j):
    # directions counter-clockwise starting from 12 o'clock
    directions = [
        [-1, 0],  # 12 o'clock
        [-1, 1],  # 1:30
        [0, 1],  # 3 o'clock
        [1, 1],  # 4:30
        [1, 0],  # 6 o'clock
        [1, -1],  # 7:30
        [0, -1],  # 9 o'clock
        [-1, -1],  # 10:30
    ]

    searchFor = ["M", "A", "S"]

    found = 0

    for direction in directions:
        d_i = i  # diff in i
        d_j = j  # diff in j

        for char in searchFor:
            d_i += direction[0]
            d_j += direction[1]
            outOfBounds = (
                d_i < 0 or d_j < 0 or d_i >= len(lines) or d_j >= len(lines[i])
            )
            if outOfBounds:
                break
            if lines[d_i][d_j] != char:
                break
            if char == searchFor[-1]:
                found += 1
    return found


def part1():
    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "X":
                sum += findMAS(i, j)
    print(sum)


part1()
