import re
import numpy as np
from numpy.linalg import svd
from mpmath import mp

file = open("data/13.txt", "r")
content = file.read()
lines = content.split("\n")


class Machine:
    def __init__(self, a, b, price):
        self.a = a
        self.b = b
        self.price = price


i = 0
machines = []
while i < len(lines):
    a = re.split(r"[+,]", lines[i])
    a = (int(a[1]), int(a[3]))
    i += 1
    b = re.split(r"[+,]", lines[i])
    b = (int(b[1]), int(b[3]))
    i += 1
    prize = re.split(r"[=,]", lines[i])
    prize = (int(prize[1]), int(prize[3]))
    i += 2
    machines.append(Machine(a, b, prize))


def part1():
    sum = 0
    for machine in machines:
        A = np.array([[machine.a[0], machine.b[0]], [machine.a[1], machine.b[1]]])
        y = np.array([machine.price[0], machine.price[1]])
        x = np.linalg.solve(A, y)
        if x[0] <= 0 or x[1] <= 0:
            continue
        if x[0] >= 100 or x[1] >= 100:
            continue

        # print(x)
        if all(list(map(lambda x: round(x, 7).is_integer(), x))):
            sum += 3 * x[0] + x[1]
    print(sum)


def part2():
    sum = 0
    for machine in machines:
        # This didn't work because of the large numbers
        A = np.array([[machine.a[0], machine.b[0]], [machine.a[1], machine.b[1]]])

        y = np.array(
            [10000000000000 + machine.price[0], 10000000000000 + machine.price[1]],
        )
        # x = np.linalg.solve(A, y)

        # Singular Value Decomposition (SVD)
        # A = U * s * Vt
        # S_inv is the inverse of s
        # Thanks to https://github.com/numpy/numpy/issues/11213 for the idea
        U, s, Vt = svd([[machine.a[0], machine.b[0]], [machine.a[1], machine.b[1]]])
        S_inv = np.diag(1 / s)
        x = (
            Vt.T
            @ S_inv
            @ U.T
            @ np.array(
                [10000000000000 + machine.price[0], 10000000000000 + machine.price[1]]
            )
        )

        if x[0] <= 0 or x[1] <= 0:
            continue
        if all(list(map(lambda x: round(x, 3).is_integer(), x))):
            sum += 3 * x[0] + x[1]
    print(round(sum, 2))


part1()
part2()
