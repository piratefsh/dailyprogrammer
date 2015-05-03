# Task: Depth-first searcher
class Node():
    def __init__(self, id):
        self.id = id
        self.children = []
    
    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return self.id

class Tree():
    def __init__(self):
        self.root = None

    # add node to tree. node is root if parent not specified
    def add(self, node_id, parent=None):
        node = Node(node_id)
        if parent is None:
            self.root = node
        else:
            parent.add_child(node)
        return node

    # do depth first search for node
    def dfs(self, target_id, curr=None):
        # start with root node
        curr = self.root if curr is None else curr

        # found
        if curr.id is target_id:
            return curr

        # recursively check children subtree
        for child in curr.children:
            found = self.dfs(target_id, child)
            if found: 
                return found

        # no match in subtree
        return None

    # recursively print tree
    def to_string(self, curr, count=0):
        indent = "-" * count
        curr_string = "\n" + indent + str(curr)
        for child in curr.children:
            curr_string += self.to_string(child, count + 1)
        return curr_string

    def __repr__(self):
        return self.to_string(self.root)

def main():
    tree = Tree()
    a = tree.add('a')
    b = tree.add('b', a)
    c = tree.add('c', a)
    g = tree.add('g', c)
    tree.add('h', g)
    tree.add('d', b)
    tree.add('e', b)
    tree.add('f', b)

    print(tree)
    print(tree.dfs('g'))

main()