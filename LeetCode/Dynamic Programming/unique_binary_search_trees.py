def numTrees(n):
    # n = 1
    # 1
    # res = 1

    # n = 2
    # 1
    #   2

    #   2
    # 1
    # res = 2

    # So we can iterate overall the numbers making them the root
    # and the sub problems will be the subtrees
    # Left sub tree = # of elements < root
    # Right sub tree = # of element > root
    # Don't have to consider element == root
    # since they are all distinct

    # Let P(i) be the number of unique subtrees for n == i

    # Base cases
    # P(0) = 1  # Include this base case to handle edge cases nicely
    # P(1) = 1

    # Recursive Case
    # P(i) = sum([P(root-1) * P(i-root) for root in range(1,i+1)])

    dp = [1] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = sum([dp[root - 1] * dp[i - root] for root in range(1, i + 1)])

    return dp[n]
