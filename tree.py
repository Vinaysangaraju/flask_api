class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(10)
left = TreeNode(5)
right = TreeNode(15)

root.left = left
root.right = right

print(root.left.data)