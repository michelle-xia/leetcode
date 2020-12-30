# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return   
        final = []
        q = []
        q.append([root, 0])
        while len(q) > 0:
            curr, level = q.pop()
            if curr:
                if len(final) == level:
                    final.append([])
                if level % 2 == 1:
                    final[level] += [curr.val]
                else:
                    final[level] = [curr.val] + final[level]
                if curr.left:
                    q.append([curr.left, level + 1])
                if curr.right:
                    q.append([curr.right, level + 1])
        return final