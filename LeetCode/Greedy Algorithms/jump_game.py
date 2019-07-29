class Solution:
    def canJump(self, nums: 'List[int]') -> bool:
        # Solution 1 - Dynamic Programming Bottom Up Approach

        # n = len(nums)

        # # Try determine whether we can reach the last index
        # # starting from the right.
        # results = [False] * n

        # # We know we can get to the last index from itself
        # # i.e. no jumps
        # results[n - 1] = True

        # for i in range(n - 2, -1, -1):
        # maxJumpIndex = min(i + nums[i], n - 1)
        # for j in range(i + 1, maxJumpIndex + 1):
        #   if results[j]:
        #       # If we can get to the end from j
        #       # and we can get to j from i
        #       # then we can get to the end from i
        #       results[i] = True
        #       break

        # return results[0]

        # Solution 2 - Greedy Approach
        n = len(nums)
        last_pos = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
