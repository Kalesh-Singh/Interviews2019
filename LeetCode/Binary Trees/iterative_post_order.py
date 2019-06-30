# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        # Solution 1 - Using 2 stacks
        # Second stack contains the post order traversal in reverse.
        stack1 = [root]
        stack2 = []

        if not root:
            return stack2

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            left_child = node.left
            right_child = node.right

            if left_child:
                stack1.append(left_child)

            if right_child:
                stack1.append(right_child)

        return [x.val for x in stack2[::-1]]
