# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
            
        temp=head
        
        
        
        before = None

        after=temp.next

        while temp:
            after=temp.next

            temp.next=before
            before=temp
            
            temp=after
    
        return before

        
        
        