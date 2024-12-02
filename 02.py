import re
from functools import reduce

file = open("data/02.txt", "r")
content = file.read()
lines = content.split("\n")

items = []
for i in range(len(lines)):
    items.append(re.split(r"\s+", lines[i]))


def inOrder(myList, decOrInc):
    sorted = myList.copy()
    sorted.sort(reverse=decOrInc < 0)

    for i in range(len(myList)):
        if myList[i] != sorted[i]:
            return False
    return True


def part1():
    safe = 0
    for i in range(len(items)):
        nums = list(map(int, items[i]))

        decOrInc = nums[1] - nums[0]

        if not inOrder(nums, decOrInc):
            continue

        for j in range(len(nums)):
            if j == 0:
                continue
            if abs(nums[j] - nums[j - 1]) < 1:
                break
            if abs(nums[j] - nums[j - 1]) > 3:
                break
            if j == len(nums) - 1:
                safe += 1

    print(safe)


def isGoodRow(myList):
    sign = 0
    # 1 for increasing, -1 for decreasing
    if myList[-1] - myList[0] > 0:
        sign = 1
    else:
        sign = -1
    for j in range(len(myList)):
        if j == 0:
            continue
        if (myList[j] - myList[j - 1]) * sign < 1 or (
            myList[j] - myList[j - 1]) * sign > 3:
            return False
    return True


def part2():
    safe = 0
    for i in range(len(items)):
        nums = list(map(int, items[i]))
        if isGoodRow(nums):
            safe += 1
        else:
            for j in range(len(nums)):
                sublist = nums[:j] + nums[j + 1 :]
                if isGoodRow(sublist):
                    safe += 1
                    break            
    print(safe)


part1()
part2()
