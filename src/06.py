# Read the file

file = open("data/06.txt", "r")
content = file.read()
lines = content.split("\n")
freshLines = lines.copy()

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


def checkIfLoop(O_loc, lines, starting_loc, dir):
    loc_now = starting_loc
    count = 0
    while True:
        next_loc = (
            loc_now[0] + directions[dir][0],
            loc_now[1] + directions[dir][1],
        )
        if not isInBounds(next_loc[0], next_loc[1]):
            return (False, None)
        char = lines[next_loc[0]][next_loc[1]]
        if char != "#" and char != "O":
            markLocationWith(lines, next_loc, "X")
            loc_now = next_loc
        else:
            dir = (dir + 1) % 4
        count += 1
        # Stupidily make sure that we have looped
        # for so long that each cell has been visited
        if count > len(lines) * len(lines[0]):
            break

    return (True, O_loc)


def part2():
    direction = 0
    lines = content.split("\n")
    loc_now = find_start_location(lines)

    obstacles_causing_loop = []

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
        linesforLoop = freshLines.copy()
        markLocationWith(linesforLoop, next_loc, "O")
        loop_check_starting_loc = find_start_location(freshLines)
        obs_loc = (next_loc[0], next_loc[1])
        if checkIfLoop(obs_loc, linesforLoop, loop_check_starting_loc, 0)[0]:
            if obs_loc not in obstacles_causing_loop:
                obstacles_causing_loop.append(next_loc)

        markLocationWith(lines, next_loc, "X")
        loc_now = next_loc
    print(len(obstacles_causing_loop))


part1()
part2()
