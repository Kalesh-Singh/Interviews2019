class Solution:
    def rob(self, nums: 'List[int]') -> int:

        # Let P(i) be the max we can rob up to index i
        # [1, 2, 3, 2, 1, 2]
        # P(0) = 1                  --> arr[i]
        # P(1) = 2                  --> max(arr[i], arr[i-1])
        # P(2) = 4 = 3 + 1          --> max(arr[i] + P(i-2), P(i-1))
        # P(3) = 2 = 2 + 2
        # P(4) = 5 = 1 + 3 + 1
        # P(5) = 6 = 2 + 2 + 2

        # Recursive
        # P(0) = arr[0]
        # P(1) = max(arr[0], arr[1])
        # P(i) = max(arr[i] + P(i-2), P(i-1))

        # [2, 1, 1, 2]
        # P(0) = 1
        # P(1) = 2
        # P(2) = 2 + 1 = 3
        # P(3) = 2 + 2 = 4

        if not nums:
            return 0

        # exclusive = P(i-1), inclusive = P(i)
        exclusive, inclusive = 0, nums[0]

        for i in range(1, len(nums)):
            inclusive, exclusive = max(exclusive + nums[i], inclusive), inclusive

        return inclusive
