import re 
file = open("data/13-example.txt", "r")
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

for machine in machines:
    print(machine.a, machine.b, machine.price)