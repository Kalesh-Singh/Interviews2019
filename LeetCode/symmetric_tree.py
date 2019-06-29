from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val \
                and self.mirror(left.left, right.right) \
                and self.mirror(left.right, right.left)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        # Solution 1 - Curr Level and Next level
        # O(n) Time, O(n) Space
        # curr_level = [root]
        # next_level = []

        # while curr_level:
        #     for node in curr_level:
        #         if node:
        #             next_level += [node.left, node.right]

        #     # If level is odd (Only the root can be an odd level)
        #     n = len(next_level)
        #     if n % 2 == 1:
        #         return False

        #     # Check that the level is a mirror
        #     i, j = 0, n-1
        #     while i < j:
        #         if next_level[i] and next_level[j]:
        #             if next_level[i].val != next_level[j].val:
        #                 return False
        #         else:
        #             if not next_level[i] and next_level[j]:
        #                 return False
        #             if next_level[i] and not next_level[j]:
        #                 return False
        #         i += 1
        #         j -= 1
        #     curr_level, next_level = next_level, []
        # return True

        # Solution 2 - Using a Queue (Similar to BFS)
        # O(n) Time, O(n) Space
        # if not root:
        #     return True

        # queue = deque()
        # queue.append(root.left)
        # queue.append(root.right)

        # while queue:
        #     left = queue.popleft()
        #     right = queue.popleft()

        #     if not left and not right:
        #         continue

        #     if not left or not right:
        #         return False

        #     if left.val != right.val:
        #         return False

        #     queue.append(left.left)
        #     queue.append(right.right)
        #     queue.append(left.right)
        #     queue.append(right.left)

        # return True
        
        # Solution 3 - Recursive
        # O(n) Time, O(1) Space (although the call stack will be a huge overhead :/)
        if not root:
            return True
        return self.mirror(root.left, root.right)
        
