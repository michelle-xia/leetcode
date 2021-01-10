# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        
        def findHeight(node):
            if node is None:
                return 0
            return 1 + max(findHeight(node.left), findHeight(node.right))
        
        left = findHeight(root.left)
        right = findHeight(root.right)
        
        ldiam = self.diameterOfBinaryTree(root.left)
        rdiam = self.diameterOfBinaryTree(root.right)
        
        return max(left + right, ldiam, rdiam)