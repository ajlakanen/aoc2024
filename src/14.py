import re

file = open("data/14-example.txt", "r")
content = file.read()
lines = content.split("\n")

GRID_SIZE = (7,11)
# GRID_SIZE = (100, 100) 

class Robot:
    def __init__(self, position, direction, grid_size):
        self.position = position
        self.direction = direction
        self.grid_size = grid_size

    
    def move(self):
        self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
        if self.position[0] + self.direction[0] > self.grid_size[0]: # down
            # self.position[0] = self.position[0] + self.direction[0] - self.grid_size[0]
            self.position = (self.position[0] + self.direction[0] - self.grid_size[0], self.position[1])
        if self.position[0] + self.direction[0] < 0: # up
            # self.position[0] = self.grid_size[0] + self.position[0] + self.direction[0]
            self.position = (self.grid_size[0] + self.position[0] + self.direction[0], self.position[1])
        if self.position[1] + self.direction[1] > self.grid_size[1]: # right
            # self.position[1] = self.position[1] + self.direction[1] - self.grid_size[1]
            self.position = (self.position[0], self.position[1] + self.direction[1] - self.grid_size[1])
        if self.position[1] + self.direction[1] < 0: # left
            # self.position[1] = self.grid_size[1] + self.position[1] + self.direction[1]
            self.position = (self.position[0], self.grid_size[1] + self.position[1] + self.direction[1])

def parse(lines):
    machines = []
    for line in lines:
        posAndDir = re.split(r"[=,\s]", line)
        position = (int(posAndDir[1]), int(posAndDir[2]))
        direction = (int(posAndDir[4]), int(posAndDir[5]))
        machines.append(Robot(position, direction, GRID_SIZE))
    return machines

def part1():
    machines = parse(lines)
    # print(machines)

    for i in range(1):
        machines[0].move()
        # print(machines[0].position)
        for j in range(GRID_SIZE[0]):
            for k in range(GRID_SIZE[1]):
                print("X" if machines[0].position == (j, k) else ".", end="")
            print("\n")

part1()
