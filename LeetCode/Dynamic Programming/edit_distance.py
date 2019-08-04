class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # Let dp[i][j] be the cost of converting
        # word1[:i+1] tp word2[:j+1]

        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | _ | _ | _ | _ |   |
        # | h | _ | _ | _ | _ |   |
        # | o | _ | _ | _ | _ |  \|/
        # | r | _ | _ | _ | _ |   i
        # | s | _ | _ | _ | _ | (End index of word1)
        # | e | _ | _ | _ | _ |

        # Note ε is the empty string.

        # Cost of converting ε to ε
        # No operations needed
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | _ | _ | _ |   |
        # | h | _ | _ | _ | _ |   |
        # | o | _ | _ | _ | _ |  \|/
        # | r | _ | _ | _ | _ |   i
        # | s | _ | _ | _ | _ | (End index of word1)
        # | e | _ | _ | _ | _ |

        # Cost of converting 'h' to ε
        # 1 Deletion needed
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | _ | _ | _ |   |
        # | h | 1 | _ | _ | _ |   |
        # | o | _ | _ | _ | _ |  \|/
        # | r | _ | _ | _ | _ |   i
        # | s | _ | _ | _ | _ | (End index of word1)
        # | e | _ | _ | _ | _ |

        # . . .

        # Cost of converting 'horse' to ε
        # 5 Deletions needed
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | _ | _ | _ |   |
        # | h | 1 | _ | _ | _ |   |
        # | o | 2 | _ | _ | _ |  \|/
        # | r | 3 | _ | _ | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting ε to 'r'
        # 1 Insertion needed
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | _ | _ |   |
        # | h | 1 | _ | _ | _ |   |
        # | o | 2 | _ | _ | _ |  \|/
        # | r | 3 | _ | _ | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # . . .

        # Cost of converting ε to 'ros'
        # 3 Insertions needed
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | _ | _ | _ |   |
        # | o | 2 | _ | _ | _ |  \|/
        # | r | 3 | _ | _ | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'h' to 'r'
        # 1 Replacement needed (Replace 'h' with 'r')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | _ | _ |   |
        # | o | 2 | _ | _ | _ |  \|/
        # | r | 3 | _ | _ | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'h' to 'ro'
        # 1 Replacement needed (Replace 'h' with 'r')
        # 1 Insertion needed (Insert 'o' after 'r')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | _ |   |
        # | o | 2 | _ | _ | _ |  \|/
        # | r | 3 | _ | _ | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'h' to 'ros'
        # 1 Replacement needed (Replace 'h' with 'r')
        # 2 Insertions needed (Insert 'os' after 'r')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | _ | _ | _ |  \|/
        # | r | 3 | _ | _ | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'ho' to 'r'
        # 1 Replacement needed (Replace 'h' with 'r')
        # 1 Deletion needed (Delete 'o')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | _ | _ |  \|/
        # | r | 3 | _ | _ | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'ho' to 'ro'
        # 1 Replacement needed (Replace 'h' with 'r')
        # (No operation needed 'o' and 'o' are the same)
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | _ |  \|/
        # | r | 3 | _ | _ | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'ho' to 'ros'
        # 1 Replacement needed (Replace 'h' with 'r')
        # (No operation needed 'o' and 'o' are the same)
        # 1 Insertion needed (Insert 's' after 'o')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | 2 |  \|/
        # | r | 3 | _ | _ | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'hor' to 'r'
        # 1 Replacement needed (Replace 'h' with 'r')
        # 2 Deletions (Delete 'or')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | 2 |  \|/
        # | r | 3 | 3 | _ | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'hor' to 'ro'
        # 1 Replacement needed (Replace 'h' with 'r')
        # (No operation needed 'o' and 'o' are the same)
        # 1 Deletion needed (Delete 'r')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | 2 |  \|/
        # | r | 3 | 3 | 2 | _ |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'hor' to 'ros'
        # 1 Replacement needed (Replace 'h' with 'r')
        # (No operation needed 'o' and 'o' are the same)
        # 1 Replacement needed (Replace 'r' with 's')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | 2 |  \|/
        # | r | 3 | 3 | 2 | 2 |   i
        # | s | 4 | _ | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'hors' to 'r'
        # 1 Replacement needed (Replace 'h' with 'r')
        # 3 Deletions needed (Delete 'ors')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | 2 |  \|/
        # | r | 3 | 3 | 2 | 2 |   i
        # | s | 4 | 4 | _ | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'hors' to 'ro'
        # 1 Replacement needed (Replace 'h' with 'r')
        # (No operation needed 'o' and 'o' are the same)
        # 2 Deletions needed (Delete 'rs')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | 2 |  \|/
        # | r | 3 | 3 | 2 | 2 |   i
        # | s | 4 | 4 | 3 | _ | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'hors' to 'ros'
        # 1 Replacement needed (Replace 'h' with 'r')
        # (No operation needed 'o' and 'o' are the same)
        # 1 Deletion needed (Delete 'r')
        # (No operation needed 's' and 's' are the same)
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | 2 |  \|/
        # | r | 3 | 3 | 2 | 2 |   i
        # | s | 4 | 4 | 3 | 2 | (End index of word1)
        # | e | 5 | _ | _ | _ |

        # Cost of converting 'horse' to 'r'
        # 1 Replacement needed (Replace 'h' with 'r')
        # 4 Deletions needed (Delete 'orse')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | 2 |  \|/
        # | r | 3 | 3 | 2 | 2 |   i
        # | s | 4 | 4 | 3 | 2 | (End index of word1)
        # | e | 5 | 5 | _ | _ |

        # Cost of converting 'horse' to 'ro'
        # 1 Replacement needed (Replace 'h' with 'r')
        # (No operation needed 'o' and 'o' are the same)
        # 3 Deletions needed (Delete 'rse')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | 2 |  \|/
        # | r | 3 | 3 | 2 | 2 |   i
        # | s | 4 | 4 | 3 | 2 | (End index of word1)
        # | e | 5 | 5 | 4 | _ |

        # Cost of converting 'horse' to 'ros'
        # 1 Replacement needed (Replace 'h' with 'r')
        # (No operation needed 'o' and 'o' are the same)
        # 1 Deletion needed (Delete 'r')
        # (No operation needed 's' and 's' are the same)
        # 1 Deletion needed (Delete 'e')
        # --------> j (End index of word2)
        # |   | ε | r | o | s |   |
        # | ε | 0 | 1 | 2 | 3 |   |
        # | h | 1 | 1 | 2 | 3 |   |
        # | o | 2 | 2 | 1 | 2 |  \|/
        # | r | 3 | 3 | 2 | 2 |   i
        # | s | 4 | 4 | 3 | 2 | (End index of word1)
        # | e | 5 | 5 | 4 | 3 |

        # Appears Recursive
        # if word1[i] == word2[j]:
        #   dp[i][j] = dp[i-1][j-1]  # No operations needed

        # else:
        # Try all possibile options
        # dp[i][j] is the min of the following
        # Replacement
        #   dp[i][j] = dp[i-1][j-1] + 1
        # Insertion
        #   dp[i][j] = dp[i][j-1] + 1
        # Deletion
        #   dp[i][j] = d[i-1][j] + 1

        # Let n be the len of word 1
        # and len m be the len of word 2
        # dp[n][m] is the solution we want
        # Notice that it is not n-1 and m-1
        # because we added extra slot for the
        # empty string edge cases.
        # We should also consider this when indexing
        # the words i.e. use i-1 and j-1 instead of
        # i and j.

        # Solution 1 - Using Dynamic Programming
        n, m = len(word1), len(word2)
        dp = [[None for _ in range(m + 1)] for _ in range(n + 1)]

        # Fill the first row
        for j in range(m + 1):
            dp[0][j] = j

        # Fill the first col
        for i in range(n + 1):
            dp[i][0] = i

        # Fill the rest of the rows in order
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[n][m]
