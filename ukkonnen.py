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

    while True:
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
            break
        #jump to next node if current node is completed
        if active_len==end and active_node.is_leaf==False:
            active_node = active_node.edge[index].next
            active_len = 0
            index = get_index(string[j+active_len])
            #if edge exist in new node
            if active_node.edge[index]!=0:
                start = active_node.edge[index].start
                end = active_node.edge[index].end
            #Rule 2: if no edge exist and node is not leaf, create new branch
            else:
                active_node.edge[index] = Edge(j + active_len + 1,i)
                break
        #rule 1 extension
        if active_len==end and active_node.is_leaf==True:
            active_node.edge[index].end = i
            break
        active_len+=1

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
print(tree.root.edge[1].start)
print(tree.root.edge[1].end)
