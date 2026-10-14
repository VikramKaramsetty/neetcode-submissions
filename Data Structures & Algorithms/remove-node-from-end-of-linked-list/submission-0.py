# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #length
        node = head
        length = 0
        while(node):
            node = node.next
            length+=1
        print(length)
        if(length == 1): return None
        if(length - n == 0):
            return head.next
        #looping from 0 to length-n
        node = head
        for i in range(length -n-1):
            node = node.next
        print(node.val)
        node.next = node.next.next

        return head
