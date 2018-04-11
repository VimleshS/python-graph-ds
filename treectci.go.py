
class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def insert(self, value):
        if self.value > value:
            if self.left_node is None:
                self.left_node = Node(value)
            else:
                # recurse
                self.left_node.insert(value)
        else:
            if self.right_node is None:
                self.right_node = Node(value)
            else:
                # recurse
                self.right_node.insert(value)

    def find(self, value):
        if value == self.value:
            return True
        if value > self.value:
            if self.right_node is not None:
                # recurse
                return self.right_node.find(value)
            else:
                return False
        else:
            if self.left_node is not None:
                # recurse
                return self.left_node.find(value)
            else:
                return False

    def printInOrder(self):
        if self.left_node is not None:
            #recurse
            self.left_node.printInOrder()
        print(self.value)
        if self.right_node is not None:
            # recurse
            self.right_node.printInOrder()


n = Node(10)
n.insert(5)
n.insert(15)
n.insert(2)
n.insert(8)
n.printInOrder()

print(n.find(15))