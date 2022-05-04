from collections import deque

class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1
 
def super_balanced(root):
    if root is None:
        return True
 
    left_side = height(root.left)
    right_side = height(root.right)
 
    if (abs(left_side - right_side) <= 0) and super_balanced(
    root.left) is True and super_balanced( root.right) is True:
        return True
 
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
test = Solution()
print(test.isSuperBalanced(root))