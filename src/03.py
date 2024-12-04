import re

file = open("data/03.txt", "r")
content = file.read()


def parseInstructions(data):
    instructions = re.findall(r"mul\(\d+,\d+\)", data)
    operandPairs = [re.findall(r"\d+", match) for match in instructions]
    return operandPairs


def part1():
    operandPairs = parseInstructions(content)
    sum = 0
    for operands in operandPairs:
        sum += int(operands[0]) * int(operands[1])
    print(sum)


def part2():
    instructions = content.split("don't()")
    sum = 0
    # Instructions before the first "don't()" are enabled
    for operands in parseInstructions(instructions[0]):
        sum += int(operands[0]) * int(operands[1])

    for a in instructions:
        dos = a.split("do()")

        # The first element is skipped
        # because it is after "don't()"
        for i in dos[1:]:
            operandPairs = parseInstructions(i)
            for operands in operandPairs:
                sum += int(operands[0]) * int(operands[1])
    print(sum)


part1()
part2()
