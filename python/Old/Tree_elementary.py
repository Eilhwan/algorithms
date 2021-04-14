class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    # def __str__(self):
    #     return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
    
    def set_root(self, node):
        self.root = node

    def make_node(self, left, data, right):
        node = Node(data)
        node.left = left
        node.right = right
        return node

    def preorder_traversal(self, node):
        if node != None:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
if __name__ == "__main__":
    # node = []
    # node.append(Node('-'))
    # node.append(Node('*'))
    # node.append(Node('/'))
    # node.append(Node('A'))
    # node.append(Node('B'))
    # node.append(Node('C'))
    # node.append(Node('D'))

    tree = Tree()
    # for i in range(len(node) // 2):
    #     tree.make_node(node[i * 2 + 1], node[i], node[i*2 + 2])

    A = tree.make_node(Node('C'), 'A', 'D')
    B = Node("B")
    root = tree.make_node(A, "-", B)
    tree.set_root(root)
    tree.preorder_traversal(tree.root)