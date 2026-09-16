class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_data=None):
        if root_data is not None:
            self.root = TreeNode(root_data)
        else:
            self.root = None

    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._print_inorder(self.root)
            print()

    def _print_inorder(self, node):
        if node is not None:
            self._print_inorder(node.left)
            print(node.data, end=" ")
            self._print_inorder(node.right)


tree = BinaryTree(10)
tree.root.left = TreeNode(5)
tree.root.right = TreeNode(15)
tree.root.left.left = TreeNode(2)
tree.root.left.right = TreeNode(7)

tree.print_tree()