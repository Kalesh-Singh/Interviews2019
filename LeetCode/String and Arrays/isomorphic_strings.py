class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Solution 1 - Check Mappings
        # O(n) Time O(n) Space
        # ns = len(s)
        # nt = len(t)

        # if ns != nt:
        #     return False

        # seen = {}
        # i = j = 0
        # while i < ns - 1:
        #     if s[i] != s[i+1] and t[j] == t[j+1]:
        #         return False
        #     if t[j] != t[j+1] and s[i] == s[i+1]:
        #         return False
        #     if s[i] != s[i+1] and t[j] != t[j+1]:
        #         if s[i] not in seen:
        #             seen[s[i]] = t[j]
        #         elif seen[s[i]] != t[j]:
        #             return False
        #     i += 1
        #     j += 1

        #     if s[i] in seen and seen[s[i]] != t[j]:
        #         return False

        # return True

        # Solution 2 - Check Mappings (Alternative Implementation)
        # O(n) Time O(n) Space
        hash_map = {}
        seen = set()

        for x, y in zip(s, t):
            if x in hash_map:
                if hash_map[x] != y:
                    return False
            else:
                if y in seen:
                    return False
                hash_map[x] = y
                seen.add(y)

        return True
