# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1
# def getNumGen(root: 'TreeNode', curr: int) -> 'generator[int]':
#     curr = curr * 10 + root.val
#     if not root.left and not root.right:
#         yield curr
#     else:
#         if root.left:
#             for x in getNumGen(root.left, curr):
#                 yield x
#         if root.right:
#             for x in getNumGen(root.right, curr):
#                 yield x

# Solution 2
# def getNums(root: 'TreeNode', nums: 'List[int]', curr: int) -> int:
#     curr = curr * 10 + root.val
#     if not root.left and not root.right:
#         nums.append(curr)
#     if root.left:
#         getNums(root.left, nums, curr)
#     if root.right:
#         getNums(root.right, nums, curr)

# Solution 3
def getSum(root: 'TreeNode', s: 'List[int]', curr: int) -> int:
    curr = curr * 10 + root.val
    if not root.left and not root.right:
        s[0] += curr
    else:
        if root.left:
            getSum(root.left, s, curr)
        if root.right:
            getSum(root.right, s, curr)


class Solution:
    def sumNumbers(self, root: 'TreeNode') -> int:
        if not root:
            return 0
        # Solution 1
        # return sum(getNumGen(root, 0))

        # Solution 2
        # nums = []
        # getNums(root, nums, 0)
        # return sum(nums)

        # Solution 3
        # Note: Integers are not passed by reference in  Python
        s = [0]
        getSum(root, s, 0)
        return s[0]
