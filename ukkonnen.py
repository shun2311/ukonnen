class Node:
    def __init__(self, previous, is_leaf = True, suffix_id=None):
        self.edge = [0]*27
        self.is_leaf = is_leaf
        self.suffix_id = suffix_id
        self.previous = previous
class Edge:
    def __init__(self, start, end, previous):
        self.start = start
        self.end = end
        self.next = Node(previous)

class End:
    def __init__(self, value):
        self.value = value

class SuffixTree:
    def __init__(self, text):
        self.root = Node(None)
        self.text = text 
        self.global_end = End(-1)
        self.active_node = self.root
        self.active_edge = None
        self.active_len = 0
        self.rule_3 = False
        self.count = 0

        self.ukkonnen()

    def get_index(self, char):
        if char != '$':
            return ord(char) - 96
        else:
            return 0 

    def edge_length(self, start, end):
        return end - start + 1
    
    def get_end(self):
        if type(self.active_edge.end) is int:
            return self.active_edge.end
        else:
            return self.active_edge.end.value
            
    def traverse(self, j, i, index):
        k = self.active_edge.start + self.active_len
        if self.text[i]!=self.text[k]:
            self.rule_3 = False
            self.active_edge.next.is_leaf = False
            self.active_edge.end = self.active_edge.start+self.active_len-1
            #old edge extension
            index = self.get_index(self.text[self.active_edge.start+self.active_len])
            self.active_edge.next.edge[index] = Edge(self.active_edge.start+self.active_len, self.global_end,self.active_node)
            #new edge extension
            index = self.get_index(self.text[i])
            self.active_edge.next.edge[index] = Edge(i, self.global_end, self.active_node)
            #return to previous node after branching
            if self.active_node.previous != None:
                self.active_node = self.active_node.previous
            self.active_len = 0
            self.count = 0
        #rule 3, do nothing
        else:
            self.rule_3 = True
            self.active_len += 1

    def skip_count(self, start, end):
        string_len = self.edge_length(start, end)
        edge_length = self.edge_length(self.active_edge.start, self.get_end())

        #skip comparison and jump to next node 
        if string_len>edge_length:
            self.count += edge_length
            self.active_node = self.active_edge.next
            #jump to new node, reset active length
            self.active_len = 0
            return True
        return False

    def ukkonnen(self):
        i = 0
        j = 0
        self.text = self.text +'$'

        while i < len(self.text):
            #Trick: rapid leaf extension
            self.global_end.value += 1
            while j<=i:
                #print("string: "+self.text[j:i+1])
                #print("previous node: "+str(self.active_node.previous))
                #print("j: "+str(j))
                #print("i: "+str(i))
                index = self.get_index(self.text[j+self.count])

                if self.active_len == 0:
                    self.active_edge = self.active_node.edge[index]
                
                #Rule 2: branch does not exist, create branch
                if self.active_edge == 0:
                    self.active_node.edge[index] = Edge(i, self.global_end, self.active_node)
                    if self.active_node.previous != None:
                        self.active_node = self.active_node.previous
                    self.count = 0
                else:
                    skip_count = self.skip_count(j,i)
                    #jump to next node and repeat the iteration
                    if skip_count:
                        continue

                    self.traverse(j, i, index)

                    #showstopper
                    if self.rule_3:
                        break
                j+=1
            i += 1

string = 'abac'
tree  = SuffixTree(string)
string = 'abaa$'
#print(tree.root.edge)
print(tree.root.edge[1].next.edge[3].start)
print(tree.root.edge[1].next.edge[3].end.value)
#print(string[tree.root.edge[1].next.edge[1].start:tree.root.edge[1].next.edge[1].end+1])
