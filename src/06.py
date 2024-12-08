# Read the file

file = open("data/06.txt", "r")
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


def find_start_location():
    for line in lines:
        for char in line:
            if char == start_char:
                start_location = (lines.index(line), line.index(char))
                return start_location
    return None


def part1():
    direction = 0

    loc_now = find_start_location()

    while True:
        next_loc = (
            loc_now[0] + directions[direction][0],
            loc_now[1] + directions[direction][1],
        )
        if not isInBounds(next_loc[0], next_loc[1]):
            print("Out of bounds", next_loc, direction)
            break
        char = lines[next_loc[0]][next_loc[1]]
        if char != "#":
            lines[next_loc[0]] = (
                lines[next_loc[0]][: next_loc[1]]
                + "X"
                + lines[next_loc[0]][next_loc[1] + 1 :]
            )
            loc_now = next_loc
        else:
            direction = (direction + 1) % 4

    # count the number of X's
    count = 0
    for line in lines:
        count += line.count("X")
    print(count)


def part2():
    direction = 0
    loc_now = find_start_location()
    count = 0

    while True:
        next_loc = (
            loc_now[0] + directions[direction][0],
            loc_now[1] + directions[direction][1],
        )
        if not isInBounds(next_loc[0], next_loc[1]):
            print("Out of bounds", next_loc, direction)
            break
        char = lines[next_loc[0]][next_loc[1]]
        if char != "#":
            lines[next_loc[0]] = (
                lines[next_loc[0]][: next_loc[1]]
                + "X"
                + lines[next_loc[0]][next_loc[1] + 1 :]
            )
            loc_now = next_loc
            count += 1
        else:
            direction = (direction + 1) % 4



part1()
