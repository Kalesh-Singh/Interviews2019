class Solution:
    def maxProduct(self, nums: 'List[int]') -> int:
        # Let F(i) be the max sub array ending at i

        # Let G(i) be the min sub array ending at i

        # Then, max(F(0), ... , F(n-1)) is the
        # answer to the problem.

        # Array | 2 | 3 | -2 |  4 |
        # Min   | 2 | 3 |-12 |-48 |
        # Max   | 2 | 6 | -2 |  4 |

        # Array | -2 |  1 | -1 |
        # Min   | -2 | -2 | -1 |
        # Max   | -2 |  1 |  2 |

        # It appears we only need to keep track of the,
        # previous max and previous min.

        # NOTE: This is just an extension of
        # Kadane's Algorithm.

        global_max = curr_max = prev_max = prev_min = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i] * prev_min, nums[i] * prev_max, nums[i])
            curr_min = min(nums[i] * prev_min, nums[i] * prev_max, nums[i])

            global_max = max(curr_max, global_max)

            prev_max, prev_min = curr_max, curr_min

        return global_max
