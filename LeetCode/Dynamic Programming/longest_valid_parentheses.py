class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # NOTE: This DP Approach did not work
        # See the solution using a stack. (Below)

        # Let's try visualizing using a table

        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | _ | _ | _ | _ | _ | _ |     |
        # | ( | _ | _ | _ | _ | _ | _ |     |
        # | ) | _ | _ | _ | _ | _ | _ |    \|/
        # | ( | _ | _ | _ | _ | _ | _ |     i
        # | ) | _ | _ | _ | _ | _ | _ | (End index of s)
        # | ) | _ | _ | _ | _ | _ | _ |

        # Let fill in for single characters
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | _ | _ | _ | _ | _ |     |
        # | ( | _ | 0 | _ | _ | _ | _ |     |
        # | ) | _ | _ | 0 | _ | _ | _ |    \|/
        # | ( | _ | _ | _ | 0 | _ | _ |     i
        # | ) | _ | _ | _ | _ | 0 | _ | (End index of s)
        # | ) | _ | _ | _ | _ | _ | 0 |

        # Let fill invalid indexes as 0 too
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | _ | _ | _ | _ | _ |     |
        # | ( | 0 | 0 | _ | _ | _ | _ |     |
        # | ) | 0 | 0 | 0 | _ | _ | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | _ | _ |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | _ | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of ')('
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | _ | _ | _ | _ |     |
        # | ( | 0 | 0 | _ | _ | _ | _ |     |
        # | ) | 0 | 0 | 0 | _ | _ | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | _ | _ |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | _ | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of '()'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | _ | _ | _ | _ |     |
        # | ( | 0 | 0 | 2 | _ | _ | _ |     |
        # | ) | 0 | 0 | 0 | _ | _ | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | _ | _ |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | _ | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |
        # If start == '(' and end == ')'
        # and longest without start == longest without end
        # Then add 2 to ???

        # Longest Valid Parenthses of ')('
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | _ | _ | _ | _ |     |
        # | ( | 0 | 0 | 2 | _ | _ | _ |     |
        # | ) | 0 | 0 | 0 | 0 | _ | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | _ | _ |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | _ | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of '()'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | _ | _ | _ | _ |     |
        # | ( | 0 | 0 | 2 | _ | _ | _ |     |
        # | ) | 0 | 0 | 0 | 0 | _ | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | _ |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | _ | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of '))'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | _ | _ | _ | _ |     |
        # | ( | 0 | 0 | 2 | _ | _ | _ |     |
        # | ) | 0 | 0 | 0 | 0 | _ | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | _ |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of ')()'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | 2 | _ | _ | _ |     |
        # | ( | 0 | 0 | 2 | _ | _ | _ |     |
        # | ) | 0 | 0 | 0 | 0 | _ | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | _ |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of '()('
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | 2 | _ | _ | _ |     |
        # | ( | 0 | 0 | 2 | 2 | _ | _ |     |
        # | ) | 0 | 0 | 0 | 0 | _ | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | _ |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of ')()'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | 2 | _ | _ | _ |     |
        # | ( | 0 | 0 | 2 | 2 | _ | _ |     |
        # | ) | 0 | 0 | 0 | 0 | 2 | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | _ |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of '())'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | 2 | _ | _ | _ |     |
        # | ( | 0 | 0 | 2 | 2 | _ | _ |     |
        # | ) | 0 | 0 | 0 | 0 | 2 | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | 2 |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of ')()('
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | 2 | 2 | _ | _ |     |
        # | ( | 0 | 0 | 2 | 2 | _ | _ |     |
        # | ) | 0 | 0 | 0 | 0 | 2 | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | 2 |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of '()()'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | 2 | 2 | _ | _ |     |
        # | ( | 0 | 0 | 2 | 2 | 4 | _ |     |
        # | ) | 0 | 0 | 0 | 0 | 2 | _ |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | 2 |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |
        # If start == '(' and end == ')'
        # and longest without start == longest without end
        # Then add 2 to longest without start or longest without end

        # Longest Valid Parenthses of ')())'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | 2 | 2 | _ | _ |     |
        # | ( | 0 | 0 | 2 | 2 | 4 | _ |     |
        # | ) | 0 | 0 | 0 | 0 | 2 | 2 |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | 2 |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of ')()()'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | 2 | 2 | 4 | _ |     |
        # | ( | 0 | 0 | 2 | 2 | 4 | _ |     |
        # | ) | 0 | 0 | 0 | 0 | 2 | 2 |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | 2 |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parenthses of '()())'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | 2 | 2 | 4 | _ |     |
        # | ( | 0 | 0 | 2 | 2 | 4 | 4 |     |
        # | ) | 0 | 0 | 0 | 0 | 2 | 2 |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | 2 |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 |
        # If start == '(' and end == ')'
        # But longest without start != longest without end
        # ans = max(longest without start, longest without end)

        # Longest Valid Parenthses of ')()())'
        # ---> j (End index of s)
        # | _ | ) | ( | ) | ( | ) | ) |     |
        # | ) | 0 | 0 | 2 | 2 | 4 | 4 |     |
        # | ( | 0 | 0 | 2 | 2 | 4 | 4 |     |
        # | ) | 0 | 0 | 0 | 0 | 2 | 2 |    \|/
        # | ( | 0 | 0 | 0 | 0 | 2 | 2 |     i
        # | ) | 0 | 0 | 0 | 0 | 0 | 0 | (End index of s)
        # If !(start == '(' and end == ')')
        # ans = max(longest without start, longest without end)

        # Let's try another example
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | _ | _ | _ | _ |
        # | ) | 0 | 0 | _ | _ | _ |
        # | ( | 0 | 0 | 0 | _ | _ |
        # | ( | 0 | 0 | 0 | 0 | _ |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parentheses of '()'
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | 2 | _ | _ | _ |
        # | ) | 0 | 0 | _ | _ | _ |
        # | ( | 0 | 0 | 0 | _ | _ |
        # | ( | 0 | 0 | 0 | 0 | _ |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parentheses of ')('
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | 2 | _ | _ | _ |
        # | ) | 0 | 0 | 0 | _ | _ |
        # | ( | 0 | 0 | 0 | _ | _ |
        # | ( | 0 | 0 | 0 | 0 | _ |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parentheses of '(('
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | 2 | _ | _ | _ |
        # | ) | 0 | 0 | 0 | _ | _ |
        # | ( | 0 | 0 | 0 | 0 | _ |
        # | ( | 0 | 0 | 0 | 0 | _ |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parentheses of '()'
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | 2 | _ | _ | _ |
        # | ) | 0 | 0 | 0 | _ | _ |
        # | ( | 0 | 0 | 0 | 0 | _ |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parentheses of '()('
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | 2 | 2 | _ | _ |
        # | ) | 0 | 0 | 0 | _ | _ |
        # | ( | 0 | 0 | 0 | 0 | _ |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parentheses of ')(('
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | 2 | 2 | _ | _ |
        # | ) | 0 | 0 | 0 | 0 | _ |
        # | ( | 0 | 0 | 0 | 0 | _ |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parentheses of '(()'
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | 2 | 2 | _ | _ |
        # | ) | 0 | 0 | 0 | 0 | _ |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parentheses of '()(('
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | 2 | 2 | 2 | _ |
        # | ) | 0 | 0 | 0 | 0 | _ |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parentheses of ')(()'
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | 2 | 2 | 2 | _ |
        # | ) | 0 | 0 | 0 | 0 | 2 |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # Longest Valid Parentheses of '()(()'
        # | _ | ( | ) | ( | ( | ) |
        # | ( | 0 | 2 | 2 | 2 | 2 |
        # | ) | 0 | 0 | 0 | 0 | 2 |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ( | 0 | 0 | 0 | 0 | 2 |
        # | ) | 0 | 0 | 0 | 0 | 0 |

        # How do we get the 2 here ? :/
        # How did we decidie it's not 4?

        # It appears we take the min of the
        # previous diagonal and add 2?

        # Appears recursive

        # Solution 1 - Dynamic Programming approach
        # if not s:
        #     return 0

        # dp = [[0 for _ in s] for _ in s]

        # # Fill in above the main diagonal
        # n = len(s)

        # for k in range(1, n):
        #     prev_min, curr_min = 0, float('inf')
        #     for i in range(n-k):
        #         j = i + k
        #         if s[i] == '(' and s[j] == ')' and dp[i][j-1] == dp[i+1][j]:
        #             dp[i][j] = prev_min + 2
        #         else:
        #             dp[i][j] = max(dp[i][j-1], dp[i+1][j], dp[i+1][j-1])

        #         curr_min = min(curr_min, dp[i][j])

        #     prev_min, curr_min = curr_min, float('inf')

        # return dp[0][n-1]

        # NOTE: This dp solution is not correct

        # ---------------------------------------------------------------
        # Solution 2 - Using a stack
        # We can remove all matched parentheses
        # and the only thing left in the stack is
        # the unmatched parentheses,
        # Then we find the max of each adjacent interval

        # stack = []
        # longest = 0
        # for i, c in enumerate(s):
        #     if c == ')':
        #         if stack and stack[-1][0] == '(':
        #             stack.pop()
        #         else:
        #             stack.append((c, i))
        #     else:
        #         stack.append((c, i))

        # # The entire string is valid
        # if not stack:
        #     return len(s)

        # # Get the interval from the start
        # start, end = 0, stack[0][1]
        # longest = max(longest, end-start)

        # n = len(stack)
        # for j in range(1, n):
        #     start, end = stack[j-1][1], stack[j][1]
        #     longest = max(longest, end-start-1)

        # # Get the interval at the end
        # start, end = stack[-1][1], len(s)-1
        # longest = max(longest, end-start)

        # return longest

        # ---------------------------------------------------------------
        # Solution 3 - This is a revision of solution 2
        # with neater code. The idea remains the same.
        # Although we do it in a single pass now :)

        stack = [('', -1)]  # Dummy entry to help with edge cases.
        longest = 0

        for i, c in enumerate(s):
            if c == ')':
                if stack[-1][0] == '(':
                    stack.pop()
                    longest = max(longest, i - stack[-1][1])
                else:
                    stack.append((c, i))
            else:
                stack.append((c, i))
        return longest
