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
        self.grid = []
        for _ in range(size[1]):
            row = []
            for _ in range(size[0]):
                row.append([])
            self.grid.append(row)

    def add(self, x, y, robot):
        self.grid[y][x].append(robot)
        pass

    def remove(self, x, y, robot):
        self.grid[y][x] = [r for r in self.grid[y][x] if r != robot]

    def get(self, x, y):
        return self.grid[y][x]

    def count(self, x, y):
        return len(self.grid[y][x])


class Robot:
    def __init__(self, position, direction, grid):
        self.X = position[0]
        self.Y = position[1]
        self.dirX = direction[0]
        self.dirY = direction[1]
        self.grid = grid

    def move(self):
        self.grid.remove(self.X, self.Y, self)
        self.X += self.dirX
        self.Y += self.dirY
        if self.X < 0:
            self.X += self.grid.size[0]
        if self.X >= self.grid.size[0]:
            self.X -= self.grid.size[0]
        if self.Y < 0:
            self.Y += self.grid.size[1]
        if self.Y >= self.grid.size[1]:
            self.Y -= self.grid.size[1]
        self.grid.add(self.X, self.Y, self)


def parse(lines, grid):
    machines = []
    for line in lines:
        posAndDir = re.split(r"[=,\s]", line)
        position = (int(posAndDir[1]), int(posAndDir[2]))  # (x, y)
        direction = (int(posAndDir[4]), int(posAndDir[5]))  # (dx, dy)
        r = Robot(position, direction, grid)
        grid.add(position[0], position[1], r)
        machines.append(r)
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
    grid = Grid(GRID_SIZE)
    machines = parse(lines, grid)

    for _ in range(100):
        for machine in machines:
            machine.move()
    multiplied = 1

    for quadrant in QUADRANTS:
        count = 0
        for x in range(quadrant[0][0], quadrant[0][1]):
            for y in range(quadrant[1][0], quadrant[1][1]):
                count += grid.count(x, y)
        multiplied *= count
    print(multiplied)


def part2():
    grid = Grid(GRID_SIZE)
    machines = parse(lines, grid)
    for i in range(100):
        print(i)
        for machine in machines:
            machine.move()
            a = countMachines(machines)
            print("counted")
            # TODO


part1()
# part2()
