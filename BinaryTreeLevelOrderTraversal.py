# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if root is None:
            return
        final = []
        q = [(root, 0)]
        while len(q) > 0:
            curr, level = q.pop(0)
            if len(final) == level:
                final.append([])
            final[level] += [curr.val]
            if curr.left:
                q.append([curr.left, level + 1])
            if curr.right:
                q.append([curr.right, level + 1])
        return final

class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        
        def traverse(node, level):
            if node is None:
                return
            if level > len(out) - 1:
                out.append([])
                
            out[level].append(node.val)
            
            traverse(node.left, level + 1) 
            traverse(node.right, level + 1)
            
        out = []
        traverse(root, 0)
        return out