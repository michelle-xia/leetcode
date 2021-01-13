# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        if root is None:
            return False
        
        def traverse(node, low, high):
            if node is None:
                return True
            
            return low < node.val < high and traverse(node.left, low, node.val) and traverse(node.right, node.val, high)
        
        return traverse(root, -math.inf, math.inf)