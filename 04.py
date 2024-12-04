import re

file = open("data/04-example.txt", "r")
content = file.read()
lines = content.split("\n")

def findMAS(i, j):
    directions = [[]]

def part1():
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'X':
                print(i, j)

    

part1()
