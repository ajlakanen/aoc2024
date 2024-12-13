file = open("data/12.txt", "r")
content = file.read()
lines = content.split("\n")


def floodFill(lines, i, j, char, replacement=" "):
    # 1. Set Q to the empty queue or stack.
    Q = []
    # 2. Add node to the end of Q.
    Q.append([i, j])
    # 3. While Q is not empty:
    while len(Q) > 0:
        # 4.   Set n equal to the first element of Q.
        n = Q[0]
        # 5.   Remove first element from Q.
        Q.pop(0)
        if n[0] < 0 or n[1] < 0 or n[0] >= len(lines) or n[1] >= len(lines[n[0]]):
            continue
        # 6.   If n is Inside:
        #        Set the n
        #        Add the node to the west of n to the end of Q.
        #        Add the node to the east of n to the end of Q.
        #        Add the node to the north of n to the end of Q.
        #        Add the node to the south of n to the end of Q.
        if lines[n[0]][n[1]] == char:
            lines[n[0]] = lines[n[0]][: n[1]] + replacement + lines[n[0]][n[1] + 1 :]
            Q.append([n[0] - 1, n[1]])  # north
            Q.append([n[0] + 1, n[1]])  # south
            Q.append([n[0], n[1] - 1])  # west
            Q.append([n[0], n[1] + 1])  # east
    # 7. Continue looping until Q is exhausted.


def getLinesWithChar(lines, char):
    charLines = []
    for line in lines:
        charLine = ""
        for c in line:
            if c != char:
                charLine += " "
            else:
                charLine += c
        charLines.append(charLine)
    return charLines


def getFirstPosition(lines, char):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == char:
                return (i, j)
    return (-1, -1)


def numOfNeighbours(lines, i, j, char):
    count = 0

    # up
    if i - 1 >= 0 and lines[i - 1][j] == char:
        count += 1
    # down
    if i + 1 < len(lines) and lines[i + 1][j] == char:
        count += 1
    # left
    if j - 1 >= 0 and lines[i][j - 1] == char:
        count += 1
    # right
    if j + 1 < len(lines[i]) and lines[i][j + 1] == char:
        count += 1
    return count


def findPerimeter(lines, char):
    perimeter = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == char:
                perimeter += 4 - numOfNeighbours(lines, i, j, char)
    return perimeter


def part1():
    # get the set of characters
    charsAndLines = {}
    for line in lines:
        for key in line:
            if key not in charsAndLines:
                charsAndLines[key] = []

    # get lines showing only the specific character
    for key in charsAndLines:
        charsAndLines[key] = getLinesWithChar(lines, key)

    # flood fill
    prices = 0
    for key in charsAndLines:
        # get the first position of the character
        (i, j) = (-1, -1)
        while getFirstPosition(charsAndLines[key], key) != (-1, -1):
            (i, j) = getFirstPosition(charsAndLines[key], key)
            floodFill(charsAndLines[key], i, j, key, "1")
            # We assume that after there are no
            # 1s outside of the flood filled area
            perimeter = findPerimeter(charsAndLines[key], "1")
            area = sum([line.count("1") for line in charsAndLines[key]])
            prices += perimeter * area
            floodFill(charsAndLines[key], i, j, "1", " ")
    print(prices)


part1()
