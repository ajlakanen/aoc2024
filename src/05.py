import functools
import itertools
import math
import pytest

# Read the file

file = open("data/05-example.txt", "r")
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

    def visit(self, node):
        if self.state[node] == 1:
            self.cycle = True
            return
        if self.state[node] == 2:
            return

        self.state[node] = 1
        for next_node in self.graph[node]:
            self.visit(next_node)

        self.state[node] = 2
        self.order.append(node)

    def createTopologicalOrder(self):
        self.state = {}
        for node in self.nodes:
            self.state[node] = 0

        self.order = []
        self.cycle = False

        for node in self.nodes:
            if self.state[node] == 0:
                self.visit(node)

        if self.cycle:
            return None
        else:
            self.order.reverse()
            return self.order


class Item:
    """Class for items in the ordering list"""
    def __init__(self, value, afters):
        self.value = value
        self.afters = afters


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
## 
    ##     # if len(list(filter(lambda item: item.value == rule[0], items))) == 0:
    ##     #     items.append(Item(rule[0], [rule[1]]))
    ##     # Otherwise update the "afters" list
    ##     #else:
    ##     #    item = list(filter(lambda item: item.value == rule[0], items))[0]
    ##     #    item.afters.append(rule[1])
## 
    ## ordering = [items[0].value]
## 
    ## # Go through all items
    ## for item in items[1:]:
    ##     # Find the index where the item should be inserted
    ##     # Start with the assumption that the item should be inserted at the end of the list
    ##     newIndex = len(ordering)
## 
    ##     # Go through all items in the ordering list
    ##     for i in range(len(ordering)): # tsekkaa mitä tapahtuu kun item.value == 66
    ##         # Go through the "afters" list of the item and check if the ccurrent element is in the list
    ##         # These are the values that should come after the item
    ##         # There are surely more efficient ways to do this, I haven't had time to think about it
    ##         for j in range(len(item.afters)):
    ##             if ordering[i] == item.afters[j]:
    ##             #if item.afters[j] == ordering[i]:
    ##                 if i < newIndex:
    ##                     newIndex = i
    ##                 break
    ##         
    ##     # Only insert if not already in the list
    ##     if item.value not in ordering:
    ##         ordering.insert(newIndex, item.value)

    # If "afters" list contains values not in the ordering list, add them to the ordering.
    # I don't think it matters if they are added in the correct order
    ## allAfters = [x for item in items for x in item.afters]
    ## filtered = list(dict.fromkeys([x for x in allAfters if x not in ordering]))
    ## ordering += filtered

    ordering = g.createTopologicalOrder()

    # For debugging: 
    # for item in items:
    #     print(item.value, item.afters)
    # print(ordering)

    valids = []
    for update in updates:
        if isUpdateValid(update, ordering):
            # print(update, "valid")
            valids.append(update)
        else:
            pass
            # print(update, "invalid")

    sum = 0
    for valid in valids:
        sum += valid[math.floor(len(valid) / 2)]
    print(sum)


part1()
