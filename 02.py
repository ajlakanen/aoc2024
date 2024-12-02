import re
from functools import reduce

file = open('data/02-example.txt', 'r')
content = file.read()
lines = content.split('\n')

items = []
for i in range(len(lines)):
    items.append(re.split(r"\s+", lines[i]))

safe = 0

for i in range(len(items)):
    nums = list(map(int, items[i]))
    nums.reduce(lambda first: )
    print(nums)


# for i in range(len(items)):
#     for j in range (len(items[i])):
#         if j == 0:
#             continue
#         if abs(int(items[i][j])-int(items[i][j-1])) < 1:
#             break
#         if abs(int(items[i][j]) - int(items[i][j])) > 3:
#             break
#     safe += 1

print(safe)