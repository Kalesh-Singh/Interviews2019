# We can use dp to solve this problem
def findLIS(s):
    n = len(s)
    dp = [1] * n
    res = 1

    for i in range(1, n):
        for j in range(0, i):
            if s[j] < s[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                res = max(res, dp[i])
    return res
