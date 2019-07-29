# Complete the jump function below.
def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    n = len(nums)

    # Try determine whether we can reach the last index
    # starting from the right.
    results = [-1] * n

    # We know we can get to the last index from itself
    # i.e. no jumps
    results[n - 1] = 0

    for i in range(n - 2, -1, -1):
        maxJumpIndex = min(i + nums[i], n - 1)
        for j in range(i + 1, maxJumpIndex + 1):
            if results[j] >= 0:
                # If we can get to the end from j
                # and we can get to j from i
                # then we can get to the end from i
                if results[i] < 0:
                    results[i] = 1 + results[j]
                else:
                    results[i] = min(1 + results[j], results[i])
    return results[0]
