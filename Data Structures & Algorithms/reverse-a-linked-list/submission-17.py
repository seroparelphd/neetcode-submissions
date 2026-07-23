# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create empty ListNode
        prev = None

        # Set current as input
        cur = head

        while cur:
            # Remember next node
            nxt = cur.next   
            
            # Make the next node the current node; reversing
            cur.next = prev  
            prev = cur

            # Move the current node forward
            cur = nxt

        return prev