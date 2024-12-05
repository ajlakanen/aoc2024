file = open("data/05-example.txt", "r")
content = file.read()
lines = content.split("\n")

rules = []
updates = []
rulesFinished = False

i = 0
while lines[i] != "":
    rule = [int(x) for x in lines[i].split("|")]
    rules.append(rule)
    i+=1
i+=1
while i < len(lines):
    line = [int(x) for x in lines[i].split(",")]
    updates.append(line)
    i+=1

# print(rules)
# print(updates)

class Item:
    def __init__ (self, value, afters):
        self.value = value
        self.afters = afters

def part1():
    items = []
    for rule in rules:
        if len(list(filter(lambda item: item.value == rule[0], items))) == 0:
            items.append(Item(rule[0], [rule[1]]))
        else:
            item = list(filter(lambda item: item.value == rule[0], items))[0]
            item.afters.append(rule[1])
    
    ordering = [items[0].value]
    
    for item in items:

        for i in range(len(ordering)):
            newIndex = -1
            for after in item.afters:
                if after == ordering[i]:
                    newIndex = i
                    break

            if newIndex == -1:
                newIndex = len(ordering)
        if item.value not in ordering:
            ordering.insert(newIndex, item.value)
    
    allAfters = [x for item in items for x in item.afters]
    filtered = list(dict.fromkeys([x for x in allAfters if x not in ordering]))
    ordering += filtered

    for item in items:
        print(item.value, item.afters)
    print(ordering)

part1()
