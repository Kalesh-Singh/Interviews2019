# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def isLeaf(node: 'TreeNode') -> bool:
    return not node.left and not node.right


class Solution:

    def hasPathSum(self, root: 'TreeNode', sum: int) -> bool:
        if not root:
            return False
        elif isLeaf(root):
            return root.val == sum
        else:
            target = sum - root.val
            return self.hasPathSum(root.left, target) \
                or self.hasPathSum(root.right, target)
