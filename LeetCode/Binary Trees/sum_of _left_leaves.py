# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: 'TreeNode') -> int:
        s = 0

        if not root:
            return 0

        stack = [root]

        while stack:
            node = stack.pop()
            left_node = node.left
            right_node = node.right

            if right_node:
                stack.append(right_node)

            if left_node:
                if not left_node.left and not left_node.right:  # If left child is a leaf
                    s += left_node.val
                else:
                    stack.append(left_node)
        return s
