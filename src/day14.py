import re
import math

file = open("data/14.txt", "r")
content = file.read()
lines = content.split("\n")

# GRID_SIZE = (11,7) # columns, rows
GRID_SIZE = (101, 103)

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for _ in range(size[0])] for _ in range(size[1])]

    def add(self, x, y, robot):
        self.grid[y][x].append(robot)

    def remove(self, x, y, robot):
        self.grid[y][x].remove(robot)

    def get(self, x, y):
        return self.grid[y][x]
    
    def count(self, x, y):
        return len(self.grid[y][x])

class Robot:
    def __init__(self, position, direction, grid_size):
        self.X = position[0]
        self.Y = position[1]
        self.dirX = direction[0]
        self.dirY = direction[1]
        self.grid_size = grid_size

    def move(self):
        self.X += self.dirX
        self.Y += self.dirY
        if self.X < 0:
            self.X += self.grid_size[0]
        if self.X >= self.grid_size[0]:
            self.X -= self.grid_size[0]
        if self.Y < 0:
            self.Y += self.grid_size[1]
        if self.Y >= self.grid_size[1]:
            self.Y -= self.grid_size[1]


def parse(lines):
    machines = []
    for line in lines:
        posAndDir = re.split(r"[=,\s]", line)
        position = (int(posAndDir[1]), int(posAndDir[2]))  # (x, y)
        direction = (int(posAndDir[4]), int(posAndDir[5]))  # (dx, dy)
        machines.append(Robot(position, direction, GRID_SIZE))
    return machines


def printMachines(machines):
    for y in range(GRID_SIZE[1]):
        line = ""
        for x in range(GRID_SIZE[0]):
            count = 0
            for machine in machines:
                if machine.X == x and machine.Y == y:
                    count += 1
            if count == 0:
                line += "."
            else:
                line += str(count)
        print(line)


def countMachines(machines):
    lines = []
    for y in range(GRID_SIZE[1]):
        line = []
        for x in range(GRID_SIZE[0]):
            count = 0
            for machine in machines:
                if machine.X == x and machine.Y == y:
                    count += 1
            line.append(count)
        lines.append(line)
    return lines


QUADRANTS = [
    [
        (0, math.floor(GRID_SIZE[0] / 2)),
        (0, math.floor(GRID_SIZE[1] / 2)),
    ],  # top left: (startX, endX), (startY, endY)
    [
        (math.ceil(GRID_SIZE[0] / 2), GRID_SIZE[0]),
        (0, math.floor(GRID_SIZE[1] / 2)),
    ],  # top right: (startX, endX), (startY, endY)
    [
        (0, math.floor(GRID_SIZE[0] / 2)),
        (math.ceil(GRID_SIZE[1] / 2), GRID_SIZE[1]),
    ],  # bottom left
    [
        (math.ceil(GRID_SIZE[0] / 2), GRID_SIZE[0]),
        (math.ceil(GRID_SIZE[1] / 2), GRID_SIZE[1]),
    ],  # bottom right
]


def part1():
    machines = parse(lines)

    for _ in range(100):
        for machine in machines:
            machine.move()
    multiplied = 1

    for quadrant in QUADRANTS:
        count = 0
        for x in range(quadrant[0][0], quadrant[0][1]):
            for y in range(quadrant[1][0], quadrant[1][1]):
                for machine in machines:
                    if machine.X == x and machine.Y == y:
                        count += 1
        multiplied *= count
    print(multiplied)


def checkIfQuadrantsMirrored(counts):
    print("checking mirroring")
    height = GRID_SIZE[1]
    width = GRID_SIZE[0]

    quadrants = [
        [
            (0, math.floor(width / 2)),
            (0, math.floor(height / 2)),
        ],  # top left: (startX, endX), (startY, endY)
        [
            (math.ceil(width / 2), width),
            (0, math.floor(height / 2)),
        ],  # top right: (startX, endX), (startY, endY)
        [
            (0, math.floor(width / 2)),
            (math.ceil(height / 2), height),
        ],  # bottom left
        [
            (math.ceil(width / 2), width),
            (math.ceil(height / 2), height),
        ],  # bottom
    ]

    # compare top left and top right
    for x in range(quadrants[0][0][0], quadrants[0][0][1]):  # top left
        for y in range(quadrants[0][1][0], quadrants[0][1][1]):
            countL = counts[y][x]
            countR = counts[y][quadrants[1][0][1] - x - 1]
            if countL != countR:
                return False
    return True


def part2():
    machines = parse(lines)
    for i in range(100):
        print(i)
        for machine in machines:
            machine.move()
            a = countMachines(machines)
            print("counted")
            if checkIfQuadrantsMirrored(a):                
                printMachines(machines)
                return


# part1()
part2()
