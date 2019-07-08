# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: 'TreeNode', k: int) -> int:
        # Solution 1 - Iterative In-order traversal
        curr = root
        stack = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            # Visit
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
