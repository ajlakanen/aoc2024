import math

# Read the file

file = open("data/05.txt", "r")
content = file.read()
lines = content.split("\n")

# Parse the input

rules = []
updates = []
rulesFinished = False

i = 0
while lines[i] != "":
    rule = [int(x) for x in lines[i].split("|")]
    rules.append(rule)
    i += 1
i += 1
while i < len(lines):
    line = [int(x) for x in lines[i].split(",")]
    updates.append(line)
    i += 1


class Graph:
    """Class for a directed graph"""
    """Thanks: Antti Laaksonen / Tietorakenteet ja algoritmit"""
    """https://tira.mooc.fi/syksy-2023/osa13/"""
    def __init__(self):
        self.nodes = []
        self.graph = {node: [] for node in self.nodes}

    def add_node(self, node):
        self.nodes.append(node)
        self.graph[node] = []

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def visit(self, node, updateNodes):
        if self.state[node] == 1:
            self.cycle = True
            return
        if self.state[node] == 2:
            return

        self.state[node] = 1
        for next_node in self.graph[node]:
            if next_node in updateNodes:
                self.visit(next_node, updateNodes)

        self.state[node] = 2
        self.order.append(node)

    def createTopologicalOrder(self, updateNodes=None):
        self.state = {}
        for node in self.nodes:
            self.state[node] = 0

        self.order = []
        self.cycle = False

        for node in self.nodes:
            if not node in updateNodes:
                continue
            if self.state[node] == 0:
                self.visit(node, updateNodes)

        if self.cycle:
            return None
        else:
            self.order.reverse()
            return self.order
    
    def count_from(self, node):
        if node in self.result:
            return self.result[node]
        
        path_count = 0
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)
        
        self.result[node] = path_count
        return path_count
        
    def count_paths(self, x, y):
        self.result = {y: 1}
        return self.count_from(x)



def isUpdateValid(update, ordering):
    """Is the update valid according to the ordering list"""
    left = 0
    for i in range(len(update)):
        for j in range(len(ordering)):
            if update[i] == ordering[j]:
                if j < left:
                    return False
                left = j
                break
    return True

def part1():
    items = []

    g = Graph()

    # Go through all rules
    for rule in rules:
        # Add the item if its value is not already in the list

        if rule[0] not in g.nodes:
            g.add_node(rule[0])
        if rule[1] not in g.nodes:
            g.add_node(rule[1])
        
        g.add_edge(rule[0], rule[1])

    valids = []
    for update in updates:
        ordering = g.createTopologicalOrder(update)
        if isUpdateValid(update, ordering):
            print(update, "valid")
            valids.append(update)
        else:
            pass
            print(update, "invalid")

    sum = 0
    for valid in valids:
        sum += valid[math.floor(len(valid) / 2)]
    print(sum)


part1()
