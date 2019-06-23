class Solution:
    def reverseWords(self, s: str) -> str:
        # SOLUTION 1
        # O(n) Time O(n) Space
        # s = s.strip().split()
        # res = [s[i] for i in range(len(s)-1,-1,-1)]
        # return ' '.join(res)

        # SOLUTION 2
        # O(n) Time O(1) Space in language where strigs are mutable
        s = list(' '.join(s.strip(' ').split()))

        # Reverse each word in place
        n = len(s)
        i = 0
        j = n - 1
        start = 0

        while start < n:
            while start < j and s[start] == ' ':
                start += 1
            end = start
            while end < j and s[end] != ' ':
                end += 1

            # Reverse word
            i1 = start
            j1 = end - 1 if s[end] == ' ' else end
            while i1 < j1:
                s[i1], s[j1] = s[j1], s[i1]
                i1 += 1
                j1 -= 1

            start = end + 1

            # Reverse the entire string
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return ''.join(s)
