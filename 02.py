import re
from functools import reduce

file = open("data/02.txt", "r")
content = file.read()
lines = content.split("\n")

items = []
for i in range(len(lines)):
    items.append(re.split(r"\s+", lines[i]))


def inOrder(list, decOrInc):
    sorted = list.copy()
    sorted.sort(reverse=decOrInc < 0)

    for i in range(len(list)):
        if list[i] != sorted[i]:
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


def inOrder2(list, ignoresLeft=1):
    i = 1
    decOrInc = 0
    while i < len(list):
        if list[i] - list[i - 1] < 0:
            if decOrInc > 0:
                if ignoresLeft == 0:
                    return False
                return inOrder2(list[:i-1] + list[i:], 0)
            else:
                decOrInc = -1
        if list[i] - list[i - 1] > 0:
            if decOrInc < 0:
                if ignoresLeft == 0:
                    return False
                return inOrder2(list[:i-1] + list[i:], 0)
            else:
                decOrInc = 1
        if list[i] - list[i-1] == 0:
            if ignoresLeft == 0:
                return False
            return inOrder2(list[:i-1] + list[i:], 0)
        i += 1
    return (True, list, ignoresLeft)


def checkIfSafe(list, ignoresLeft=1):
    for i in range(len(list)):
        if i == 0:
            continue
        if abs(list[i] - list[i - 1]) < 1:
            if ignoresLeft == 0 or i == len(list) - 1:
                return False
            else:
                return checkIfSafe(list[:i] + list[i + 1 :], 0)

        if abs(list[i] - list[i - 1]) > 3:
            if ignoresLeft == 0 or i == len(list) - 1:
                return False
            else:
                return checkIfSafe(list[:i] + list[i + 1 :], 0)
    return True


def part2():
    safe = 0
    for i in range(len(items)):
        nums = list(map(int, items[i]))
        
        checkOrder = inOrder2(nums, 1)

        if checkOrder==False:
            continue

        if checkIfSafe(checkOrder[1], checkOrder[2]):
            safe += 1

    print(safe)


part1()
part2()
