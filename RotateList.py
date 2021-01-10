# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        if head is None:
            return   
        if head.next is None:
            return head
        curr= head
        count = 1
        # find size of list
        while curr.next:
            count += 1
            curr = curr.next
        k %= count
        
        for _ in range(k):
            curr = head
            while curr.next:
                if curr.next.next is None:
                    start = ListNode(curr.next.val)
                    curr.next = None
                    break
                curr = curr.next
            start.next = head
            head = start
        return head

class Solution2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k is None or k == 0:
            return head
        
        size = 1
        tail = head
        newTail = head
        
        while tail.next:           
            size += 1         
            if size > k + 1:
                newTail = newTail.next
            tail = tail.next
        
        if size < k:
            return self.rotateRight(head, k % size)
        elif size == k:
            return head
        else:
            newHead, newTail.next = newTail.next, None
            tail.next = head
            return newHead