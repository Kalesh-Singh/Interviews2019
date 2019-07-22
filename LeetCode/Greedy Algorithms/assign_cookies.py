class Solution:
    def findContentChildren(self, g: 'List[int]', s: 'List[int]') -> int:
        # Solution 1 - Greedy Approach
        # O(nlogn) Time  O(1) Space
        g.sort()
        s.sort()

        greed_idx = cookie_idx = content_count = 0

        while greed_idx < len(g) and cookie_idx < len(s):
            if g[greed_idx] <= s[cookie_idx]:
                content_count += 1
                greed_idx += 1
                cookie_idx += 1
            elif s[cookie_idx] < g[greed_idx]:
                cookie_idx += 1

        return content_count
