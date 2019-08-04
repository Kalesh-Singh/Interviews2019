class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # Let P(i) be the problem of finding the longest
        # palindormic subsequence of s[i:]

        # The P(0) is the solution we want.

        # At every i we have a choice of whether to
        # include that character or not.

        # P(i) = ???
        # Not sure how to combine subproblems :/

        # "cbbd"
        # | c | b | b | d |
        # | _ | _ | _ | 1 |
        # | c | b | b | d |
        # | 2 | 2 | 1 | 1 |

        # "cbbdc"
        # | c | b | b | d | c |
        # | _ | _ | _ | _ | 1 |
        # | c | b | b | d | c |
        # | 4 | 2 | 1 | 1 | 1 |

        # "cbdbc"
        # | c | b | d | b | c |
        # | _ | _ | _ | _ | 1 |
        # | c | b | d | b | c |
        # | 4 | 3 | 1 | 1 | 1 |

        # Keep track of the right of the subsequence?
        # Check if letter also exists on the right of the
        # current subsequence to know if to add to length?

        # Not sure if that would be the easiest thing
        # to code or if it has any performance benefits
        # from the naive approach :/

        # Let's try to visualize with a table
        # Maybe we will see a pattern.

        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | _ | _ | _ | _ | _ |     |
        # | b | _ | _ | _ | _ | _ |     |
        # | b | _ | _ | _ | _ | _ |    \|/
        # | d | _ | _ | _ | _ | _ |     i
        # | c | _ | _ | _ | _ | _ | (Start index of string)

        # Fill in for length of 1
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | _ | _ | _ | _ |     |
        # | b | _ | 1 | _ | _ | _ |     |
        # | b | _ | _ | 1 | _ | _ |    \|/
        # | d | _ | _ | _ | 1 | _ |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'cb'
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | 1 | _ | _ | _ |     |
        # | b | _ | 1 | _ | _ | _ |     |
        # | b | _ | _ | 1 | _ | _ |    \|/
        # | d | _ | _ | _ | 1 | _ |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'bb'
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | 1 | _ | _ | _ |     |
        # | b | _ | 1 | 2 | _ | _ |     |
        # | b | _ | _ | 1 | _ | _ |    \|/
        # | d | _ | _ | _ | 1 | _ |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)
        # NOTE: Interesting case here

        # Longest palindromic subsequence of 'bd'
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | 1 | _ | _ | _ |     |
        # | b | _ | 1 | 2 | _ | _ |     |
        # | b | _ | _ | 1 | 1 | _ |    \|/
        # | d | _ | _ | _ | 1 | _ |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'dc'
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | 1 | _ | _ | _ |     |
        # | b | _ | 1 | 2 | _ | _ |     |
        # | b | _ | _ | 1 | 1 | _ |    \|/
        # | d | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'cbb'
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | 1 | 2 | _ | _ |     |
        # | b | _ | 1 | 2 | _ | _ |     |
        # | b | _ | _ | 1 | 1 | _ |    \|/
        # | d | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'bbd'
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | 1 | 2 | _ | _ |     |
        # | b | _ | 1 | 2 | 2 | _ |     |
        # | b | _ | _ | 1 | 1 | _ |    \|/
        # | d | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'bdc'
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | 1 | 2 | _ | _ |     |
        # | b | _ | 1 | 2 | 2 | _ |     |
        # | b | _ | _ | 1 | 1 | 1 |    \|/
        # | d | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'cbbd'
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | 1 | 2 | 2 | _ |     |
        # | b | _ | 1 | 2 | 2 | _ |     |
        # | b | _ | _ | 1 | 1 | 1 |    \|/
        # | d | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'bbdc'
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | 1 | 2 | 2 | _ |     |
        # | b | _ | 1 | 2 | 2 | 2 |     |
        # | b | _ | _ | 1 | 1 | 1 |    \|/
        # | d | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'cbbdc'
        # ---> j (End index of string)
        # |   | c | b | b | d | c |
        # | c | 1 | 1 | 2 | 2 | 4 |     |
        # | b | _ | 1 | 2 | 2 | 2 |     |
        # | b | _ | _ | 1 | 1 | 1 |    \|/
        # | d | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # It appears promising
        # We can now see how to combine the subproblems
        # We need the solution to the subproblem exclulding
        # the start character and  end character,
        # including the start character and excluding the end character,
        # and excluding the start character and including the
        # end character.

        # Let's try another example to be certain

        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | _ | _ | _ | _ | _ |     |
        # | b | _ | _ | _ | _ | _ |     |
        # | d | _ | _ | _ | _ | _ |    \|/
        # | d | _ | _ | _ | _ | _ |     i
        # | c | _ | _ | _ | _ | _ | (Start index of string)

        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | _ | _ | _ | _ |     |
        # | b | _ | 1 | _ | _ | _ |     |
        # | d | _ | _ | 1 | _ | _ |    \|/
        # | b | _ | _ | _ | 1 | _ |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Fill in for length of 1
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | _ | _ | _ | _ |     |
        # | b | _ | 1 | _ | _ | _ |     |
        # | d | _ | _ | 1 | _ | _ |    \|/
        # | b | _ | _ | _ | 1 | _ |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'cb'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | _ | _ | _ |     |
        # | b | _ | 1 | _ | _ | _ |     |
        # | d | _ | _ | 1 | _ | _ |    \|/
        # | b | _ | _ | _ | 1 | _ |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'bd'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | _ | _ | _ |     |
        # | b | _ | 1 | 1 | _ | _ |     |
        # | d | _ | _ | 1 | _ | _ |    \|/
        # | b | _ | _ | _ | 1 | _ |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'db'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | _ | _ | _ |     |
        # | b | _ | 1 | 1 | _ | _ |     |
        # | d | _ | _ | 1 | 1 | _ |    \|/
        # | b | _ | _ | _ | 1 | _ |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'bc'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | _ | _ | _ |     |
        # | b | _ | 1 | 1 | _ | _ |     |
        # | d | _ | _ | 1 | 1 | _ |    \|/
        # | b | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'cbd'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | 1 | _ | _ |     |
        # | b | _ | 1 | 1 | _ | _ |     |
        # | d | _ | _ | 1 | 1 | _ |    \|/
        # | b | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'bdb'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | 1 | _ | _ |     |
        # | b | _ | 1 | 1 | 3 | _ |     |
        # | d | _ | _ | 1 | 1 | _ |    \|/
        # | b | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)
        # NOTE: Interesting case here

        # Longest palindromic subsequence of 'dbc'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | 1 | _ | _ |     |
        # | b | _ | 1 | 1 | 3 | _ |     |
        # | d | _ | _ | 1 | 1 | 1 |    \|/
        # | b | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'cbdb'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | 1 | 3 | _ |     |
        # | b | _ | 1 | 1 | 3 | _ |     |
        # | d | _ | _ | 1 | 1 | 1 |    \|/
        # | b | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'bdbc'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | 1 | 3 | _ |     |
        # | b | _ | 1 | 1 | 3 | 3 |     |
        # | d | _ | _ | 1 | 1 | 1 |    \|/
        # | b | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'bdbc'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | 1 | 3 | _ |     |
        # | b | _ | 1 | 1 | 3 | 3 |     |
        # | d | _ | _ | 1 | 1 | 1 |    \|/
        # | b | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Longest palindromic subsequence of 'cbdbc'
        # ---> j (End index of string)
        # |   | c | b | d | b | c |
        # | c | 1 | 1 | 1 | 3 | 5 |     |
        # | b | _ | 1 | 1 | 3 | 3 |     |
        # | d | _ | _ | 1 | 1 | 1 |    \|/
        # | b | _ | _ | _ | 1 | 1 |     i
        # | c | _ | _ | _ | _ | 1 | (Start index of string)

        # Appears Recursive
        # if s[i] == s[j]:
        #   if j - i == 1:      # 2 Chars
        #       dp[i][j] = 2
        #   elif j -  i == 2:   # 3 Chars
        #       dp[i][j] == 3
        #   else:
        #       dp[i][j] = 2 + dp[i+1][j-1] without start and without end
        # else:
        #   dp[i][j] = max(dp[i][j-1]  # Including start char and excluding end char
        #                   dp[i+1][j] # Excluding start char and excluding end char

        # Create Table
        dp = [[0 for _ in s] for _ in s]

        n = len(s)

        # Fill in the main diagonal
        for i in range(n):
            dp[i][i] = 1

        # Fill in the diagonals above the main diagonal
        for k in range(1, n):
            for i in range(n - k):
                j = i + k
                if s[i] == s[j]:
                    if j - i == 1:  # 2 chars
                        dp[i][j] = 2
                    elif j - i == 2:  # 3 chars
                        dp[i][j] = 3
                    else:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    # Max of these:
                    # Including start char and excluding end char
                    # Excluding start char and excluding end char
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][n - 1]

    # For debugging
    def printTable(self, s, table):
        print('_', end='\t')
        for c in s:
            print(c, end='\t')
        print()
        for row, c in zip(table, s):
            print(c, end='\t')
            for x in row:
                print(x, end='\t')
            print()
        print()
