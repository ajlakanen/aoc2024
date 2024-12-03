import re

file = open("data/03-example2.txt", "r")
content = file.read()

def part1():  
    instructions = re.findall(r"mul\(\d+,\d+\)", content)
    operandPairs =  [re.findall(r"\d+", match) for match in instructions]
    sum = 0
    for operands in operandPairs:
        sum += int(operands[0]) * int(operands[1])
    print(sum)

def part2():
    instructions = content.split("don't()")
    print(instructions)
    for a in instructions:
        dos = a.split("do()")
        for i in dos[1:]:
            print (i)

part1()
part2()