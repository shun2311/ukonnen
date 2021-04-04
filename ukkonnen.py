class Tree:
    def __init__(self):
        self.root = Node()

class Node:
    def __init__(self, is_leaf = True, suffix_id=None):
        self.edge = [0]*27
        self.is_leaf = is_leaf
        self.suffix_id = suffix_id

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next = Node()

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
                active_node.edge[index] = Edge(j, i)
            #traverse through tree
            #else:
                #complete_traverse = False
                #while not complete_traverse:

            j+=1
        j = 0
        i += 1
    return tree

tree  = ukkonnen("abc")
print(tree.root.edge[2].start)
print(tree.root.edge[2].end)
