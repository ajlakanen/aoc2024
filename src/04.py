file = open("data/04.txt", "r")
content = file.read()
lines = content.split("\n")


def findMAS(i, j):
    # directions counter-clockwise starting from 12 o'clock
    directions = [
        [-1, 0],  # 12 o'clock
        [-1, 1],  # 1:30
        [0, 1],  # 3 o'clock
        [1, 1],  # 4:30
        [1, 0],  # 6 o'clock
        [1, -1],  # 7:30
        [0, -1],  # 9 o'clock
        [-1, -1],  # 10:30
    ]

    searchFor = ["M", "A", "S"]

    found = 0

    for direction in directions:
        d_i = i  # diff in i
        d_j = j  # diff in j

        for char in searchFor:
            d_i += direction[0]
            d_j += direction[1]
            outOfBounds = (
                d_i < 0 or d_j < 0 or d_i >= len(lines) or d_j >= len(lines[i])
            )
            if outOfBounds:
                break
            if lines[d_i][d_j] != char:
                break
            if char == searchFor[-1]:
                found += 1
    return found


def part1():
    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "X":
                sum += findMAS(i, j)
    print(sum)


def checkSquareAround(i, j):
    howManyFound = 0
    directions = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
    for direction in directions:
        d_i = i + direction[0]
        d_j = j + direction[1]
        outOfBounds = (
            d_i < max(0, i - 2)
            or d_j < max(0, j - 2)
            or d_i > min(len(lines) - 1, i + 2)
            or d_j > min(len(lines[i]) - 1, j + 2)
        )
        if outOfBounds:
            continue
        # At the center should be "A"
        if lines[d_i][d_j] != "A":
            continue
        # Check three corners
        corners = [
            [2 * direction[0], 0],
            [0, 2 * direction[1]],
            [2 * direction[0], 2 * direction[1]],
        ]
        chars = ""
        for corner in corners:
            outOfBounds = (
                i + corner[0] < 0
                or j + corner[1] < 0
                or i + corner[0] >= len(lines)
                or j + corner[1] >= len(lines[i])
            )
            if outOfBounds:
                continue
            chars += lines[i + corner[0]][j + corner[1]]
        if "".join(sorted(chars)) == "MSS":
            # M can not be at the opposite corner
            oppositeCorner = lines[i + corners[2][0]][j + corners[2][1]]
            if oppositeCorner == "M":
                continue
            howManyFound += 1
    return howManyFound


def part2():
    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "M":
                sum += checkSquareAround(i, j)
    print(sum / 2)


part1()
part2()
