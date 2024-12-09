# Read the file

file = open("data/06-example.txt", "r")
content = file.read()
lines = content.split("\n")

# Parse the input
start_char = "^"
start_location = (0, 0)

directions = [
    (-1, 0),  # 12 o'clock
    (0, 1),  # 3 o'clock
    (1, 0),  # 6 o'clock
    (0, -1),  # 9 o'clock
]


def isInBounds(i, j):
    return i >= 0 and j >= 0 and i < len(lines) and j < len(lines[i])


def find_start_location(lines):
    for line in lines:
        for char in line:
            if char == start_char:
                start_location = (lines.index(line), line.index(char))
                return start_location
    return None


def part1():
    direction = 0
    loc_now = find_start_location(lines)
    while True:
        next_loc = (
            loc_now[0] + directions[direction][0],
            loc_now[1] + directions[direction][1],
        )
        if not isInBounds(next_loc[0], next_loc[1]):
            break
        char = lines[next_loc[0]][next_loc[1]]
        if char != "#":
            markLocationWith(lines, next_loc, "X")
            loc_now = next_loc
        else:
            direction = (direction + 1) % 4

    # count the number of X's
    count = 0
    for line in lines:
        count += line.count("X")
    print(count)


def markLocationWith(lines, location, char):
    lines[location[0]] = (
        lines[location[0]][: location[1]] + char + lines[location[0]][location[1] + 1 :]
    )


def checkIfLoop(lines, starting_loc, direction):
    loc_now = starting_loc
    count = 0
    while True:
        next_loc = (
            loc_now[0] + directions[direction][0],
            loc_now[1] + directions[direction][1],
        )
        if not isInBounds(next_loc[0], next_loc[1]):
            return False
        char = lines[next_loc[0]][next_loc[1]]
        if char != "#" and char != "O":
            markLocationWith(lines, next_loc, "X")
            loc_now = next_loc
        else:
            direction = (direction + 1) % 4
        count += 1
        if count > len(lines) * len(lines[0]):
            break
    for line in lines:
        print(line)
    print("\n")

    return True


def part2():
    direction = 0
    lines = content.split("\n")
    loc_now = find_start_location(lines)
    count = 0

    while True:
        next_loc = (
            loc_now[0] + directions[direction][0],
            loc_now[1] + directions[direction][1],
        )

        if not isInBounds(next_loc[0], next_loc[1]):
            break

        char = lines[next_loc[0]][next_loc[1]]
        if char == "#" or char == "O":
            direction = (direction + 1) % 4
            continue

        # Insert an obstacle and check if that causes a loop
        markLocationWith(lines, next_loc, "O")

        loop_check_starting_loc = (loc_now[0], loc_now[1])
        loopLines = lines.copy()
        if checkIfLoop(loopLines, loop_check_starting_loc, direction):
            count += 1

        markLocationWith(lines, next_loc, "X")
        loc_now = next_loc
    print(count)


part1()
part2()
