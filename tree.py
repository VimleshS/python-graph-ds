class Node:
    def __init__(self, val):
        self.value = val
        self.node = None

    def add(self, node):
        self.node = node

    def get(self):
        if self.node:
            return self.node

n = Node('A')
n2 = Node(2)
n.add(n2)
n6 = Node('X')
n2.add(n6)
n4 = Node(4)
n6.add(n4)

def process(node):
    if not node:
        return
    print(node.value)
    n = node.get()
    process(n)

process(n)
