file = open("data/12-example3.txt", "r")
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

def part1():
    for line in lines:
        print(line)

    # get all different characters from lines
    charsAndLines = {}
    for line in lines:
        for key in line:
            if key not in charsAndLines:
                charsAndLines[key] = []

    print(charsAndLines)

    for key in charsAndLines:
        charLines = []
        for line in lines:
            charLine = ""
            for c in line:
                if c != key:
                    charLine += " "
                else:
                    charLine += c
            charLines.append(charLine)
        charsAndLines[key] = charLines
        for line in charsAndLines[key]:
            print(line)
        # lines = floodFill(lines, 1, 2, "O")
        # for line in lines:
        #    print(line)
    floodFill


part1()
