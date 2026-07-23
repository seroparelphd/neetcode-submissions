# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If tree empty
        if not root:
            return[]
        
        result = []
        # Initialize queue (deque) with root
        queue = deque([root])

        while queue:
            # How many nodes in level?
            level_size = len(queue)
            print(f"[DEBUG] level_size = {level_size}")
            # print(f"[DEBUG] level_size = {level_size}")
            current_level_vals = []

            # Process nodes only in this level
            for _ in range(level_size):
                print(f"[DEBUG] _ = {_}")
                # Pop node from left side
                # popped = self.left.pop()
                popped = queue.popleft()
                print(f"[DEBUG] popped.val = {popped.val}") # {popped}")
                # Add its value
                current_level_vals.append(popped.val)
                # Add children to queue for next level 
                if popped.left:
                    queue.append(popped.left)
                    print(f"[DEBUG] popped.left = {popped.left.val}")
                if popped.right:
                    queue.append(popped.right)
                    print(f"[DEBUG] popped.right = {popped.right.val}")

            # Add completed level to result list
            print(f"[DEBUG] current_level_vals = {current_level_vals}")
            result.append(current_level_vals)
            print(f"[DEBUG] result = {result}")
        return result