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
    count = 0
    while j+count<=i:
        #rule 2
        if string[j+count]!=string[start+active_len]:
            old_end = end
            #set new end for old branch
            active_node.edge[index].is_leaf = False
            active_node.edge[index].end = start+active_len-1
            #set new active node to branch out
            active_node = active_node.edge[index].next
            index = get_index(string[start+active_len])
            active_node.edge[index] = Edge(start+active_len, end)
            index = get_index(string[j+count])
            active_node.edge[index] = Edge(j+count, i)
            return
        #reach end of edge, move to next node
        if start+active_len == end:
            active_node = active_node.edge[index].next
            index = get_index(string[j+count+1])
            #Rule 2: branch does not exist, extend branch from node
            if active_node.edge[index] == 0:
                active_node.edge[index] = Edge(j+count+1,i)
                return
            #else continue to traverse through tree
            active_len=0
            count+=1
            start = active_node.edge[index].start
            end = active_node.edge[index].end
            continue
        active_len+=1
        count+=1
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

string = 'abaa'
tree  = ukkonnen(string)
string = 'abaa$'
#print(tree.root.edge)
print(tree.root.edge[1].next.edge[0].start)
print(tree.root.edge[1].next.edge[0].end)
#print(string[tree.root.edge[1].next.edge[1].start:tree.root.edge[1].next.edge[1].end+1])
