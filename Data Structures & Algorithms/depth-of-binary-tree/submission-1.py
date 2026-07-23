# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case: An empty tree has a depth of 0
        if not root:
            return 0
        
        level = 0
        # Initialize queue with the root node
        queue = deque([root])
        
        while queue:
            # PhD Key Learning: Capture the current size.
            # This 'freezes' the number of nodes at this specific depth
            level_size = len(queue)
            
            for _ in range(level_size):
                # Process only the nodes belonging to the current level
                node = queue.popleft()
                
                # Add children to the queue for the NEXT level traversal
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # After the for-loop, we have finished one entire horizontal level
            level += 1
            
        return level