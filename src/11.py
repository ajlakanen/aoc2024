# Read and parse the file

file = open("data/11.txt", "r")
content = file.read()
nums = list(map(lambda x: int(x), content.split(' ')))

print(nums)

def getLength(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

def part1():
    i = 0
    numsNow = nums.copy()

    while i < 25:
        nextNums = []
        for j in range(len(numsNow)):
            if numsNow[j] == 0:
                nextNums.append(1)
            elif getLength(numsNow[j]) %2 == 0:
                # cut in half
                length = getLength(numsNow[j]) 
                left = numsNow[j] // (10 ** (length // 2))
                right = numsNow[j] % (10 ** (length // 2))
                nextNums.append(left)
                nextNums.append(right)
            else:
                nextNums.append(numsNow[j] * 2024)
        numsNow = nextNums
        i += 1
    print(len(numsNow))

def add(dict, key, value):
    if key in dict:
        dict[key] += value
    else:
        dict[key] = value

def handle(keysAndValues):
    keysAndValuesNow = keysAndValues.copy()
    for key in keysAndValues:
        if key == 0:
            add(keysAndValuesNow, 1, keysAndValues[key])
            keysAndValuesNow[key] -= keysAndValues[key]
        elif getLength(key) % 2 != 0:
            add(keysAndValuesNow, key * 2024, keysAndValues[key])
            keysAndValuesNow[key] -= keysAndValues[key]
        else:
            # cut in half
            length = getLength(key)
            left = key // (10 ** (length // 2))
            right = key % (10 ** (length // 2))
            add(keysAndValuesNow, left, keysAndValues[key])
            add(keysAndValuesNow, right, keysAndValues[key])
            keysAndValuesNow[key] -= keysAndValues[key]

    return keysAndValuesNow

def part2():
    keysAndValues = {}
    for num in nums:
        keysAndValues[num] = 1

    for _ in range(75):
        keysAndValues = handle(keysAndValues)

    print(sum(keysAndValues.values()))

part1()
part2()
