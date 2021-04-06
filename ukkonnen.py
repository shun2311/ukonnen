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

class End:
    def __init__(self, value):
        self.value = value

class SuffixTree:
    def __init__(self, text):
        self.root = Node()
        self.text = text 
        self.global_end = End(-1)

        self.ukkonnen()

    def get_index(self, char):
        if char != '$':
            return ord(char) - 96
        else:
            return 0 

    def traverse(self, active_node, index, j, i): 
        active_len = 0
        start = active_node.edge[index].start
        if type(active_node.edge[index].end) is int:
            end = active_node.edge[index].end
        else:
            end = active_node.edge[index].end.value
        count = 0
        
        while j+count<=i:
            #rule 2
            if self.text[j+count]!=self.text[start+active_len]:
                #set new end for old branch
                active_node.edge[index].next.is_leaf = False
                active_node.edge[index].end = start+active_len-1
                #set new active node to branch out
                active_node = active_node.edge[index].next
                index = self.get_index(self.text[start+active_len])
                active_node.edge[index] = Edge(start+active_len, self.global_end)
                index = self.get_index(self.text[j+count])
                active_node.edge[index] = Edge(j+count, self.global_end)
                return
            
            #reach end of edge, move to next node
            if start+active_len == end and j+count<i:
                active_node = active_node.edge[index].next
                index = self.get_index(self.text[j+count+1])
                #Rule 2: branch does not exist, extend branch from node
                if active_node.edge[index] == 0:
                    active_node.edge[index] = Edge(j+count+1,self.global_end)
                    return
                #else continue to traverse through tree
                active_len=0
                count+=1
                start = active_node.edge[index].start
                if type(active_node.edge[index].end) is int:
                    end = active_node.edge[index].end
                else:
                    end = active_node.edge[index].end.value
                continue
            active_len+=1
            count+=1
        
    def ukkonnen(self):
        i = 0
        #phase 0
        active_node = self.root
        self.text = self.text +'$'

        while i < len(self.text):
            j = 0

            #rapid leaf extension trick
            self.global_end.value += 1
            while j<=i:
                active_node = self.root
                index = self.get_index(self.text[j])
                #Rule 2
                if active_node.edge[index]==0:
                    active_node.edge[index] = Edge(j, self.global_end)
                else:
                    self.traverse(active_node,index, j, i)    
                j+=1
            i += 1

string = 'abaa'
tree  = SuffixTree(string)
string = 'abaa$'
#print(tree.root.edge)
<<<<<<< Updated upstream
print(tree.root.edge[0].start)
print(tree.root.edge[0].end.value)
=======
print(tree.root.edge[1].next.edge[2].start)
print(tree.root.edge[1].next.edge[2].end.value)
>>>>>>> Stashed changes
#print(string[tree.root.edge[1].next.edge[1].start:tree.root.edge[1].next.edge[1].end+1])
