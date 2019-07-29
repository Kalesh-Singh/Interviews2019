from collections import defaultdict
from bisect import bisect_right


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Solution 1 - Keeping track of Indexes of Character occurences in the search string.
        # O(mlogn) Time O(n) space where n is the length of t and m is the length of s
        # This is an answer to the follow up.
        # The answer to the original question is trivial and can be accomplished using
        # a 2 pointer techinique in O(n) time.

        idx = defaultdict(list)
        for i, c in enumerate(t):
            idx[c].append(i)

        prev = -1
        for i, c in enumerate(s):
            j = bisect_right(idx[c], prev)
            if j == len(idx[c]):
                return False
            prev = idx[c][j]
        return True
