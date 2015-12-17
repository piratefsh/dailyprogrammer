class Node:
    def __init__(self, id, neighbours=[]):
        self.id = id
        self.neighbours = neighbours

    def add(self, node):
        self.neighbours.append(node)

    def remove(self, id):
        for n in self.neighbours:
            if n.id == id: self.neighbours.remove(n) 
    def __repr__(self):
        n_ids = map(lambda n: n.id, self.neighbours)
        return "%s: [%s]" % (self.id, ", ".join(n_ids))

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def __repr__(self):
        return "\n".join([str(node) for node in self.nodes])


def main():
    a = Node('a')
    b = Node('b')
    a.add(b)
    graph = Graph([a, b])

    print(a)
    print(graph)
    print('--')

main()