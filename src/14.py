import re
import math

file = open("data/14.txt", "r")
content = file.read()
lines = content.split("\n")

# GRID_SIZE = (11,7) # columns, rows
GRID_SIZE = (101, 103)

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
        position = (int(posAndDir[1]), int(posAndDir[2])) # (x, y)
        direction = (int(posAndDir[4]), int(posAndDir[5])) # (dx, dy)
        machines.append(Robot(position, direction, GRID_SIZE))
    return machines

def part1():
    machines = parse(lines)

    for _ in range(100):
        for machine in machines:
            machine.move()
    for y in range(GRID_SIZE[1]):
        line =""
        for x in range(GRID_SIZE[0]):
            count = 0
            for machine in machines:
                if machine.X == x and machine.Y == y:
                    count += 1
                #if count == 0:
                    # print(".")
                    #line += "."
                #else: 
                    # print(count)
                    #line += str(count)
            #print(line)
        # input()
    #print("---")

    quadrants =[
        [(0, math.floor(GRID_SIZE[0] / 2)), (0, math.floor(GRID_SIZE[1] / 2))], # top left
        [(math.ceil(GRID_SIZE[0] / 2), GRID_SIZE[0]), (0, math.floor(GRID_SIZE[1] / 2))], # top right
        [(0, math.floor(GRID_SIZE[0] / 2)), (math.ceil(GRID_SIZE[1] / 2), GRID_SIZE[1])], # bottom left
        [(math.ceil(GRID_SIZE[0] / 2), GRID_SIZE[0]), (math.ceil(GRID_SIZE[1] / 2), GRID_SIZE[1])] # bottom right
    ]

    multiplied = 1

    for quadrant in quadrants:
        count = 0
        for x in range(quadrant[0][0], quadrant[0][1]):
            for y in range(quadrant[1][0], quadrant[1][1]):
                for machine in machines:
                    if machine.X == x and machine.Y == y:
                        count += 1
        multiplied *= count

    # count = 1
    # countNow= 0
    # for x in range(math.floor(GRID_SIZE[0] / 2)):
    #     for y in range(math.floor(GRID_SIZE[1] / 2)):
    #         for machine in machines:
    #             if machine.X == x and machine.Y == y:
    #                 countNow += 1
    # count *= countNow
# 
    # countNow = 0
    # for x in range(math.ceil(GRID_SIZE[0] / 2), GRID_SIZE[0]):
    #     for y in range(math.ceil(GRID_SIZE[1] / 2)):
    #         for machine in machines:
    #             if machine.X == x and machine.Y == y:
    #                 countNow += 1
    # count *= countNow
# 
    # countNow = 0
    # for x in range(math.floor(GRID_SIZE[0] / 2)):
    #     for y in range(math.ceil(GRID_SIZE[1] / 2), GRID_SIZE[1]):
    #         for machine in machines:
    #             if machine.X == x and machine.Y == y:
    #                 countNow += 1
    # count *= countNow
# 
    # countNow = 0
    # for x in range(math.ceil(GRID_SIZE[0] / 2), GRID_SIZE[0]):
    #     for y in range(math.ceil(GRID_SIZE[1] / 2), GRID_SIZE[1]):
    #         for machine in machines:
    #             if machine.X == x and machine.Y == y:
    #                 countNow += 1
    # count *= countNow
    print(multiplied)


part1()
