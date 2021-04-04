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
            active_node = tree.root
            index = get_index(string[j])
            #Rule 2
            if active_node.edge[index]==0:
                active_node.edge[index] = Edge(j, i)
            #traverse through tree
            else:
                active_len = 0
                start = active_node.edge[index].start
                end = active_node.edge[index].end
                while active_len < end - start:
                    #Rule 2 branch from edge
                    if string[start+active_len]!=string[j+active_len]:
                        old_end = end
                        branch_start = start
                        #update end 
                        active_node.edge[index].end = start + active_len
                        active_node.edge[index].is_leaf = False
                        index = get_index(string[start + active_len + 1])
                        #extend old string
                        active_node.edge[index] = Edge(start + active_len + 1,end)
                        #branch for new suffix
                        index = get_index(string[j + active_len])
                        active_node.edge[index] = Edge(j + active_len + 1,i)
                    active_len+=1
                #Rule 1 
                if active_node.edge[index].next.is_leaf:
                    active_node.edge[index].end = i

            j+=1
        j = 0
        i += 1
    return tree

tree  = ukkonnen("abaa")
#print(tree.root.edge)
print(tree.root.edge[2].start)
print(tree.root.edge[2].end)
