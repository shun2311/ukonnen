class Tree:
    def __init__(self):
        self.root = Node()

class Node:
    def __init__(self):
        self.edge = [0]*27
        
class Edge:
    def __init__(self, string):
        self.string = string
        self.next = Node()
    
    def __str__(self):
        return self.string