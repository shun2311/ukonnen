import suffix_tree

def traverse(string, suffix):
    i = 0
    while i<len(suffix) and string[i]==suffix[i]:
        i+=1
    return i

def build_suffix_tree(string):
    tree = suffix_tree.Tree()

    i = 0
    j = 0

    while i<len(string):
        index = ord(string[i]) - 96

        if tree.root.edge[index]==0:
            text = string[i:len(string)]+'$'
            tree.root.edge[index] = suffix_tree.Edge(text, suffix_tree.Node())

        else:
            text = tree.root.edge[index].string
            suffix = string[i:len(string)]+"$"
            branch_index = traverse(text, suffix)
            #create new edge
            if branch_index!=len(suffix) - 1:
                char_index = ord(suffix[branch_index]) - 96
            else:
                char_index = 0
            branch_text = suffix[branch_index:len(suffix)]
            tree.root.edge[index].next.edge[char_index] = suffix_tree.Edge(branch_text, suffix_tree.Node())

            #split branch
            

        i+=1
    return tree


text = "abaa"
tree = build_suffix_tree(text)
print(tree.root.edge[1].next.edge[1].string)

