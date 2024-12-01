import re

file = open('data/01.txt', 'r')
content = file.read()
lines = content.split('\n')
list1 = []
list2 = []

for i in range(len(lines)):
    items = re.split(r"\s+", lines[i])
    list1.append(items[0])
    list2.append(items[1])

list1.sort()
list2.sort()

def part1():
    distance = 0
    for i in range(len(list1)):
        distance += abs(int(list1[i]) - int(list2[i]))
    print(distance)

def part2():
    total = 0
    for i in range(len(list1)):
        times = 0
        for j in range(len(list2)):
            if list2[j] < list1[i]:
                continue
            if list2[j] > list1[i]:
                break
            if list2[j] == list1[i]:
                times += 1
        total += int(list1[i]) * times
    print(total)

part1()
part2()
