# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        # Solution 1 - Preorder Traversal
        # O(n) Time O(1) Space
        # if root:
        #     root.left, root.right = root.right, root.left
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        # return root
        
        # Solution 2 - Curr Level and Next Level
        # O(n) Time O(n) Space
        curr_level = [root]
        next_level = []
        while curr_level:
            for node in curr_level:
                if node:
                    node.left, node.right = node.right, node.left
                    next_level += [node.left, node.right]
            curr_level, next_level = next_level, []
        return root
        
