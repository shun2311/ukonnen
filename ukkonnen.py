import suffix_tree
def traverse(node,suffix):
    if suffix[0]!='$':
        index = ord(suffix[0]) - 96
    else:
        index = 0
    active_node = node
    if active_node.edge[index]==0:
        return active_node

def build_suffix_tree(string):
    i = 0
    string = string+"$"
    tree = suffix_tree.Tree()
    while i<len(string):
        suffix = string[i:len(string)]
        node = tree.root
        active_node = traverse(node,suffix)
        if suffix[0]!='$':
            index = ord(suffix[0]) - 96
        else:
            index = 0
        if active_node != None:
            active_node.edge[index] = suffix_tree.Edge(suffix, suffix_tree.Node())
        i+=1
    
    return tree

text = "abaa"
tree = build_suffix_tree(text)
print(tree.root.edge[0])

