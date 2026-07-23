# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # some list to store values

        def dfs(node):
            # base case: if node is None, just return
            if not node:
                return

            # 1) traverse left
            dfs(node.left)

            # 2) visit node (append its value to res)
            res.append(node.val)

            # 3) traverse right
            dfs(node.right)

        dfs(root)
        return res
