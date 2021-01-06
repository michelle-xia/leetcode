# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        
        def traverse(l, r):
            if l is None or r is None:
                return l == r
            if l.val != r.val:
                return False
            
            return traverse(l.left, r.right) and traverse(l.right, r.left)
        
        return traverse(root.left, root.right)