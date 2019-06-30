# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def isZeros(root: 'TreeNode') -> bool:
    if not root.right and not root.left:
        return root.val == 0
    else:
        # We would have already removed the children if
        # they were zeros (Pre-order Traversal)
        return False


class Solution:
    def pruneTree(self, root: 'TreeNode') -> 'TreeNode':
        # SOLUTION 1 - Pre-order Traversal
        if root:
            left = root.left
            right = root.right

            self.pruneTree(left)
            self.pruneTree(right)

            if left and isZeros(left):
                root.left = None

            if right and isZeros(right):
                root.right = None

        return root
