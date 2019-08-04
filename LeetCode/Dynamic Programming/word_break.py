class Solution:
    def wordBreak(self, s: str, wordDict: 'List[str]') -> bool:
        # wordDict = [beaten, encounter, counter, beat]
        # s = "beatencounter"

        # Let P(i) be the solution to s[i:]
        # P(0) is the solution to the overall problem
        #  ___________________________________________________
        # | b | e | a | t | e | n | c | o | u | n | t | e | r |
        #
        # Is 'r' in dict?
        # ___________________________________________________
        # | b | e | a | t | e | n | c | o | u | n | t | e | F |
        #
        # Is 'er' in dict? No need to check if 'e' in dict since 'r' is not.
        #  ___________________________________________________
        # | b | e | a | t | e | n | c | o | u | n | t | F | F |
        #
        # Is 'ter' in dict? No need to check if 't' in dict since 'er' is not.
        #  ___________________________________________________
        # | b | e | a | t | e | n | c | o | u | n | F | F | F |
        #
        # Is 'nter' in dict? No need to check if 't' in dict since 'er' is not.
        #  ___________________________________________________
        # | b | e | a | t | e | n | c | o | u | F | F | F | F |
        #
        # . . .
        #
        # Is 'ounter' in dict? No need to check if 'o' in dict since 'unter' is not.
        #  ___________________________________________________
        # | b | e | a | t | e | n | c | F | F | F | F | F | F |
        #
        # Is 'counter' in dict? No need to check if 'c' in dict since 'ounter' is not.
        #  ___________________________________________________
        # | b | e | a | t | e | n | T | F | F | F | F | F | F |
        #
        # Is 'n' or 'ncounter' in dict?
        #  ___________________________________________________
        # | b | e | a | t | e | F | T | F | F | F | F | F | F |
        #
        # Is 'en' or 'encounter' in dict?
        #  ___________________________________________________
        # | b | e | a | t | T | F | T | F | F | F | F | F | F |
        #
        # Is 't', 'ten' or 'tencounter' in dict?
        #  ___________________________________________________
        # | b | e | a | F | T | F | T | F | F | F | F | F | F |
        #
        # Is 'at', 'aten' or 'atencounter' in dict?
        #  ___________________________________________________
        # | b | e | F | F | T | F | T | F | F | F | F | F | F |
        #
        # Is 'eat', 'eaten' or 'eatencounter' in dict?
        #  ___________________________________________________
        # | b | F | F | F | T | F | T | F | F | F | F | F | F |
        #
        # Is 'beat', 'beaten' or 'beatencounter' in dict?
        #  ___________________________________________________
        # | T | F | F | F | T | F | T | F | F | F | F | F | F |

        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True  # To handle edge case of first word

        for i in range(n - 1, -1, -1):
            for end in range(i, n + 1):
                if dp[end]:
                    if s[i:end] in wordDict:
                        dp[i] = True
                        break
        return dp[0]
