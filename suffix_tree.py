class Tree:
    def __init__(self):
        self.root = Node()

class Node:
    def __init__(self):
        self.edge = [0]*26

class Edge:
    def __init__(self, string, next_node=None):
        self.string = string
        self.next = next_node