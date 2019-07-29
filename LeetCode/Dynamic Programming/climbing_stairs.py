class Solution:
    def climbStairs(self, n: int) -> int:
        # Solution 1 - Dynamic Programming Approach

        # n = 1
        # 1         --> 1

        # n = 2
        # 1 1       --> 1 + res[1]
        # 2

        # n = 3
        # 1 1 1     --> res[2] + res[1]
        # 1 2
        # 2 1

        # n = 4
        # 1 1 1 1   --> res[3] + res[2]
        # 1 1 2
        # 1 2 1
        # 2 1 1
        # 2 2

        # Recursive in nature
        # Repeated sub-problems, for instance res[2] and res[1]
        # Linear --> No table required

        # Looks very similar to fibonacci

        n_2 = 1
        n_1 = 2

        if n < 3:
            return n

        for i in range(2, n):
            res = n_1 + n_2
            n_1, n_2 = res, n_1

        return res
