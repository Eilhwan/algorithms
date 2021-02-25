
class Node:
    
    def __init__(self, data):
        self.item = data
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def make_node(self, left, data, right):
        node = Node(data)
        node.left = left
        node.right = right
        return node

    def inorder_traversal(self, root):
        if root != None:
            self.inorder_traversal(root.left)
            print(root.item, end='')
            self.inorder_traversal(root.right)
    def preorder_traversal(self, root):
        if root != None:
            print(root.item, end='')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
    def postorder_traversal(self, root):
        if root != None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.item, end='')
   



# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .


if __name__ == "__main__":
    n = int(input())

    nodes = []
    for i in range(n):
        data, left, right = input().split()
        nodes.append([data, left, right])

    t = Tree()
    for i in range(n):
        data, left, right = nodes.pop()
        if data == "A":
            t.set_root(t.make_node(Node(left), data, Node(right)))
        else:
            t.make_node(t.make_node(Node(left), data, Node(right)))

    t.preorder_traversal(t.get_root())


