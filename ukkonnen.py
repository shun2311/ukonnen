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

def get_index(char):
    if char != '$':
        return ord(char) - 96
    else:
        return 0   

def traverse(active_node,index, string, j, i): 
    active_len = 0
    start = active_node.edge[index].start
    end = active_node.edge[index].end

    while active_len<=start-end:
        if string[j+active_len]!=string[start+active_len]:
            return
        active_len+=1
    active_node.edge[index].end = i

def ukkonnen(string):
    i = 0
    #phase 0
    tree = Tree()
    active_node = tree.root
    string = string +'$'

    while i < len(string):
        j = 0
        while j<=i:
            active_node = tree.root
            index = get_index(string[j])
            #Rule 2
            if active_node.edge[index]==0:
                active_node.edge[index] = Edge(j, i)
            else:
                traverse(active_node,index, string, j, i)    
            j+=1
        i += 1
    return tree

tree  = ukkonnen("abaa")
#print(tree.root.edge)
print(tree.root.edge[2].start)
print(tree.root.edge[2].end)
