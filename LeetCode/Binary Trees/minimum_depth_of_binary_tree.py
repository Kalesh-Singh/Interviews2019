# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isLeaf(node: 'TreeNode') -> bool:
    return not node.left and not node.right


class Solution:
    def minDepth(self, root: 'TreeNode') -> int:
        # SOLUTION 1 - Level Order Traversal
        depth = 0

        if not root:
            return depth

        curr_level = [root]
        while curr_level:
            depth += 1
            next_level = []

            for node in curr_level:
                if isLeaf(node):
                    return depth
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            curr_level = next_level
