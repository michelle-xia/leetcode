# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        # create list out of linkedlist
        l = []
        while head:
            l.append(head.val)
            head = head.next
        if len(l) == 0:
            return
        mid = len(l) // 2
        node = TreeNode(l[mid])
        node.left = self.helper(l[:mid])
        node.right = self.helper(l[mid + 1:])
        return node
    
    def helper(self, l):
        if len(l) == 0:
            return
        mid = len(l) // 2
        node = TreeNode(l[mid])
        node.left = self.helper(l[:mid])
        node.right = self.helper(l[mid + 1:])
        return node