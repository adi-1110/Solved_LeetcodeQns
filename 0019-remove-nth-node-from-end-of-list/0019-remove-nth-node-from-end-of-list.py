# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        prev=None
        curr=end=head
        

        for _ in range(n-1):
            end=end.next
        
        while end.next:
            if prev is None:
                prev=head
            else:
                prev=prev.next
            curr=curr.next
            end=end.next
        
        if prev is None:
            return head.next
        
        prev.next=curr.next
        curr.next=None
        return head

        