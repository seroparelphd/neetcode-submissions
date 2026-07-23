# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If tree empty
        if not root:
            return 0

        depth = 0
        queue = deque([root])
        print(f"queue = {[node.val for node in queue]}")
        while queue:
            level_size = len(queue)
            print(f"level_size = {level_size}")
            for _ in range(level_size):
                node = queue.popleft()
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
            print(f"depth = {depth}")

        return depth