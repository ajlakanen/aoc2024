# Read the file

file = open("data/06-example.txt", "r")
content = file.read()
lines = content.split("\n")

# Parse the input

start_char = "^"
start_location = (0, 0)


def find_start_location():
    for line in lines:
        for char in line:
            if char == start_char:
                start_location = (lines.index(line), line.index(char))
                return start_location
    return None


def isInBounds(i, j):
    return i >= 0 and j >= 0 and i < len(lines) and j < len(lines[i])


def part1():
    loc_now = find_start_location()
    direction = (-1, 0)
    while True:
        loc_now = (loc_now[0] + direction[0], loc_now[1] + direction[1])
        if not isInBounds(loc_now[0], loc_now[1]):
            break
        char = lines[loc_now[0]][loc_now[1]]
        print(char)
        if char == "#":
            print(direction)
            direction_x = -1 if direction[1] == 1 else direction[1] + 1
            # direction_y = (-1 + direction[0] + 1) % 2 + 1
            direction_y = -1 if direction[0] == 1 else direction[0] + 1
            print(direction_y, direction_x)
            break


part1()
