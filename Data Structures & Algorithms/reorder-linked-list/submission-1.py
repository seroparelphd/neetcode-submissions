# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []      # To access a node by index
        current = head  # Point to 1st node
        while current:
            nodes.append(current)
            current = current.next
            # print(current)
        # print(nodes)
        i, j = 0, len(nodes) - 1    # Pointers
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next = None


