class Solution:
    def longestPalindrome(self, s: str) -> str:
        # https://guides.codepath.org/compsci/DP-Table
        # Solution 1 - Dynamic Programming
        # This problem illustrates a nice technique for
        # filling the diagonals of a dp table.

        # -----> j (end index)
        # | _ | b | a | b | a | d |     |
        # | b | F | F | F | F | F |     |
        # | a | F | F | F | F | F |     |
        # | b | F | F | F | F | F |    \|/
        # | a | F | F | F | F | F |     i
        # | d | F | F | F | F | F | (start index)

        # Fill in True for single letter
        # | _ | b | a | b | a | d |
        # | b | T | F | F | F | F |
        # | a | F | T | F | F | F |
        # | b | F | F | T | F | F |
        # | a | F | F | F | T | F |
        # | d | F | F | F | F | T |

        # Fill in for 2 letter s[i] == s[j]
        # | _ | b | a | b | a | d |
        # | b | T | F | F | F | F |
        # | a | F | T | F | F | F |
        # | b | F | F | T | F | F |
        # | a | F | F | F | T | F |
        # | d | F | F | F | F | T |

        # Fill in the other diagonals
        # s[i][j] = s[i] == s[j] and s[i+1][j-1]
        # | _ | b | a | b | a | d |
        # | b | T | F | F | F | F |
        # | a | F | T | F | F | F |
        # | b | F | F | T | F | F |
        # | a | F | F | F | T | F |
        # | d | F | F | F | F | T |

        if not s or len(s) == 1:
            return s

        n = len(s)

        dp = [[False for _ in s] for _ in s]

        # Fill in the main diagonal for single letter substring
        for i in range(n):
            dp[i][i] = True

        longest = (0, 1)

        # Fill in the diagonals above the main diagonal
        for k in range(1, n):
            for i in range(n - k):
                j = i + k

                if k == 1:  # 2 letters
                    is_p = s[i] == s[j]
                else:
                    is_p = s[i] == s[j] and dp[i + 1][j - 1]
                if is_p:
                    longest = (i, j + 1)
                dp[i][j] = is_p
        start, end = longest
        return s[start:end]
