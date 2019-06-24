# Given a sequence of integers a1, a2, ... an. A 132 pattern is a
# subsequence ai, aj, ak, such that i < j < k and ai < ak < aj.

def find132pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    if not nums:
        return False

    n = len(nums)

    if n < 3:
        return False

    min_left = [None] * n
    min_right = [None] * n

    min_left[0] = nums[0]
    for i in range(1, n):
        min_left[i] = min(min_left[i - 1], nums[i])

    min_right[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], nums[i])

    for j in range(1, n - 1):
        if nums[j] > min_left[j - 1] and nums[j] > min_right[j + 1]:
            return True
    return False
