# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return
        
        if len(lists) == 1:
            return lists[0]
        
        # add all values to one list
        l = []
        
        for ll in lists:
            while ll:
                l.append(ll.val)
                ll = ll.next
        
        l.sort()
        
        if len(l) == 0:
            return
        
        head = ListNode(l[0])
        curr = head
        del l[0]
        
        for num in l:
            node = ListNode(num)
            curr.next = node
            curr = curr.next
            
        return head
            
        