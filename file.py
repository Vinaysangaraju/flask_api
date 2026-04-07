class tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

n1 = tree(20)
n2 = tree (10)
n3 = tree(30)
n1.left = n2
n1.right = n3

print(n1.data)
print(n1.left.data)
print(n1.right.data)