# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        def traverse(node, right):
            if node:
                node.next = right
                traverse(node.left, node.right)
                traverse(node.right, right.left if right else None)
            return node
        return traverse(root, None)