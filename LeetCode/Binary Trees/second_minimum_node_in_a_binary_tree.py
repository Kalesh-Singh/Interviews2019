# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findSecondMinimumValue(self, root: 'TreeNode') -> int:
        if not root:
            return -1

        self.second_min = float('inf')
        min_val = root.val

        def dfs(node: 'TreeNode'):
            if node:
                if min_val < node.val < self.second_min:
                    self.second_min = node.val
                elif node.val == min_val:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)

        return self.second_min if self.second_min < float('inf') else -1
