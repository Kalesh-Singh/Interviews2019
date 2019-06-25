# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Returns height of tree rooted at node if it is balanced
    # else returns -1.
    def balanced(self, node: 'TreeNode', heights: dict) -> int:
        if not node:
            heights[node] = 0
            return 0
        left_height = heights[node.left] if node.left in heights else self.balanced(node.left, heights)
        if left_height == -1:
            heights[node] = -1
            return -1
        right_height = heights[node.right] if node.right in heights else self.balanced(node.right, heights)
        if right_height == -1:
            heights[node] = -1
            return -1
        if abs(left_height - right_height) > 1:
            heights[node] = -1
            return -1
        node_height = 1 + max(left_height, right_height)
        heights[node] = node_height
        return node_height
    
    def isBalanced(self, root: 'TreeNode') -> bool:
        heights = {}
        return self.balanced(root, heights) != -1
