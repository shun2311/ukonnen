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

class SuffixTree:
    def __init__(self, text):
        self.tree = Tree()
        self.text = text 
        
        self.ukkonnen()

    def traverse(self, active_node, index, j, i): 
        active_len = 0
        start = active_node.edge[index].start
        end = active_node.edge[index].end
        count = 0
        
        while j+count<=i:
            #rule 2
            if self.text[j+count]!=self.text[start+active_len]:
                old_end = end
                #set new end for old branch
                active_node.edge[index].next.is_leaf = False
                active_node.edge[index].end = start+active_len-1
                #set new active node to branch out
                active_node = active_node.edge[index].next
                index = get_index(self.text[start+active_len])
                active_node.edge[index] = Edge(start+active_len, end)
                index = get_index(self.text[j+count])
                active_node.edge[index] = Edge(j+count, i)
                return
            
            #reach end of edge, either:
            #1) extend leaf
            #2) move to next node
            if start+active_len == end and j+count<i:
                #Rule 1: reach a leaf, extend the leaf
                if active_node.edge[index].next.is_leaf and i-(j+count)==1:
                    active_node.edge[index].end = i
                    return
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

    def ukkonnen(self):
        i = 0
        #phase 0
        active_node = self.tree.root
        self.text = self.text +'$'

        while i < len(self.text):
            j = 0
            while j<=i:
                active_node = self.tree.root
                index = get_index(self.text[j])
                #Rule 2
                if active_node.edge[index]==0:
                    active_node.edge[index] = Edge(j, i)
                else:
                    self.traverse(active_node,index, j, i)    
                j+=1
            i += 1

string = 'abac'
suffix_tree  = SuffixTree(string)
string = 'abaa$'
#print(tree.root.edge)
print(suffix_tree.tree.root.edge[0].start)
print(suffix_tree.tree.root.edge[0].end)
#print(string[tree.root.edge[1].next.edge[1].start:tree.root.edge[1].next.edge[1].end+1])
