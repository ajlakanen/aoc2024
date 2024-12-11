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
        # print(numsNow)
        i += 1
    print(len(numsNow))

part1()