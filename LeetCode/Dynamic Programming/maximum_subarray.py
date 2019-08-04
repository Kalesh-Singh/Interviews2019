class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        # Solution 1 - Using Kadane's Algorithm

        # [-2, 1, -3, 4, -1, 2]
        # Let P(i) be the maximum subarray ending at index i
        # P(0) = [-2]
        # P(1) = [1]
        # P(2) = [1, -3]
        # P(3) = [4]
        # P(4) = [4, -1]
        # P(5) = [4, -1 , 2]

        # Appears recursive
        # P(0) = arr[0]
        # P(i) = max(arr[i], arr[i] + P(i-1)) for i > 0

        # The maximum sub-array is the max of these local maxes.
        # NOTE: This is known as Kadane's Algorithm.

        local_max = global_max = nums[0]

        for i in range(1, len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(global_max, local_max)

        return global_max
