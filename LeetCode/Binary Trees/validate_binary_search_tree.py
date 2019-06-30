# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> bool:

        # Solution 1 - Recursion
        # def valid(node: 'TreeNode', lower=float('-inf'), upper=float('inf')):
        #     if not node:
        #         return True

        #     val = node.val

        #     if val <= lower or val >= upper:
        #         return False

        #     if not valid(node.right, val, upper):
        #         return False

        #     if not valid(node.left, lower, val):
        #         return False

        #     return True

        # return valid(root)

        # Solution 2 - Iterative
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, lower, upper = stack.pop()

            if not node:
                continue

            val = node.val

            if val <= lower or val >= upper:
                return False

            stack.append((node.right, val, upper))
            stack.append((node.left, lower, val))

        return True
