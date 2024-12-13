import re 
import numpy as np

file = open("data/13.txt", "r")
content = file.read()
lines = content.split("\n")

class Machine:
    def __init__(self, a,b, price):
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
    i+= 1   
    prize = re.split(r"[=,]", lines[i])
    prize = (int(prize[1]), int(prize[3]))
    i += 2
    machines.append(Machine(a,b,prize))

sum = 0
for machine in machines:
    # print(machine.a, machine.b, machine.price)
    A = np.array([[machine.a[0], machine.b[0]], [machine.a[1], machine.b[1]]])
    y = np.array([machine.price[0], machine.price[1]])
    x = np.linalg.solve(A, y)
    if x[0] <= 0 or x[1] <= 0:
        continue
    if x[0] >= 100 or x[1] >= 100:
        continue

    print(x)
    if all(list(map(lambda x: round(x, 7).is_integer(), x))):
        sum += 3 * x[0] + x[1]
    
print(sum)