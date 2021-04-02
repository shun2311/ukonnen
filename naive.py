import ukkonnen

def get_index(char):
    if char != '$':
        return ord(char) - 96
    else:
        return 0

def traverse(node,suffix):
    active_node = node
    active_len = 0
    i = 0
    index = get_index(suffix[0])

    if active_node.edge[index]==0:
        return (i, active_len, active_node)
    else:
        string = active_node.edge[index].string
    while i<len(suffix):
        active_len = 0
        #traverse through current edge
        while active_len<len(string):
            #branch at edge
            if string[active_len]!=suffix[i]:
                return (i, active_len, active_node)
            active_len += 1
            i+=1
        index = get_index(string[active_len-1])
        active_node = active_node.edge[index].next
        index = get_index(suffix[i])
        #if branch does not exist branch from the current active node
        if active_node.edge[index]==0:
            return (i, active_len, active_node)


def build_suffix_tree(string):
    i = 0
    string = string+"$"
    tree = ukkonnen.Tree()
    while i<len(string):
        suffix = string[i:len(string)]
        node = tree.root
        traverse_tuple = traverse(node,suffix)
        suffix_index = traverse_tuple[0]
        active_len = traverse_tuple[1]
        active_node = traverse_tuple[2]
        index = get_index(suffix[0])

        #branch from node
        if active_len == 0:
            active_node.edge[index] = ukkonnen.Edge(suffix)
        #branch from edge
        else:
            text_branch = active_node.edge[index].string
            before_branch = text_branch[0:active_len]
            after_branch = text_branch[active_len:len(text_branch)]
            suffix_branch = suffix[suffix_index:len(suffix)]
            active_node.edge[index].string = before_branch
            char_index = get_index(after_branch[0])
            active_node.edge[index].next.edge[char_index] = ukkonnen.Edge(after_branch)
            char_index = get_index(suffix_branch[0])
            print("suffix_branch: "+suffix_branch)
            print("char_index: "+str(char_index))
            active_node.edge[index].next.edge[char_index] = ukkonnen.Edge(suffix_branch)
        i+=1
    return tree

text = "abaa"
tree = build_suffix_tree(text)
#print(tree.root.edge[1].next.edge)

