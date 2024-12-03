import re

file = open("data/03.txt", "r")
content = file.read()

def part1():  
    instructions = []
    matches = re.findall(r"mul\(\d+,\d+\)", content)
    operandPairs =  [re.findall(r"\d+", match) for match in matches]
    sum = 0
    for operands in operandPairs:
        sum += int(operands[0]) * int(operands[1])
    print(sum)

part1()
