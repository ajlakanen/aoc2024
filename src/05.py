file = open("data/05-example.txt", "r")
content = file.read()
lines = content.split("\n")

rules = []
updates = []
rulesFinished = False

for i in len(lines):
    if lines[i] == "":
        rulesFinished = True
    rule = [int(x) for x in lines[i].split("|")]
    rules.append(rule)
    i+=1

i+=1
while i < len(lines):
    line = [int(x) for x in lines[i].split(",")]
    updates.append(line)
    i+=1

print(updates)

class Item:
    def __init__ (self, value, after):
        self.value = value
        self.after = after

def part1():
    ordering = []
    for rule in rules:
        if len(list(filter(lambda item: item.value == rule[0], ordering))) == 0:
            ordering.append(Item(rule[0], [rule[1]]))
        else:
            item = list(filter(lambda item: item.value == rule[0], ordering))[0]
            item.after.append(rule[1])
        
    
    
    # map(lambda item: print(item.value, item.after), ordering)
    # ordering.map(lambda item: print(item.value, item.after))
    # print(ordering)

part1()
