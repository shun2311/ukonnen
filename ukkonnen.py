class Tree:
    def __init__(self):
        self.root = Node()

class Node:
    def __init__(self, is_leaf = True, suffix_id=None):
        self.edge = [0]*27
        self.is_leaf = is_leaf
        self.suffix_id = suffix_id

class Edge:
    def __init__(self, string):
        self.string = string
        self.next = Node()
    
    def __str__(self):
        return self.string

def rule_1():
    return True

def get_index(char):
    if char != '$':
        return ord(char) - 96
    else:
        return 0    
def ukkonnen(string):
    i = 0
    j = 0
    #phase 0
    tree = Tree()
    active_node = tree.root
    string = string +'$'

    while i < len(string):
        while j<=i:
            index = get_index(string[j])
            #Rule 2
            if active_node.edge[index]==0:
                active_node.edge[index] = Edge(string[j:i+1])
            j+=1
        j = 0
        i += 1
    return tree

tree  = ukkonnen("abc")
print(tree.root.edge[])
