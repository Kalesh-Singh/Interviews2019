class Solution:
    def numDecodings(self, s: str) -> int:
        # A -> 1
        # B -> 2
        # C -> 3
        # D -> 4
        # E -> 5
        # ...
        # V -> 22
        # W -> 23
        # X -> 24
        # Y -> 25
        # z -> 26

        # "4"
        # D

        # "34"
        # C D
        # > 26

        # "234"
        # B C D
        # W D

        # "1234"
        # A B C D
        # A W D
        # L C D

        # "21234"
        # B A B C D
        # B A W D
        # B L C D
        # U B C D
        # U W D

        # "321234"
        # C B A B C D
        # C B A W D
        # C B L C D
        # C U B C D
        # C U W D
        # > 26

        # We can use a recursive approach

        # Figure out the edge cases with zeros
        # "01"
        # 0

        # "0"
        # Invalid --> 0

        # "10"
        # J

        # "101"
        # J A

        # "202"
        # T B

        # "301"
        # Invalid --> 0

        # 0 is only valid when preceded by a 2 or 1
        # i.e 10 and 20

        # Any string with 0 at the beginning cannot be represented
        # i.e 0 ways

        # Appears recursive in nature

        # Base Cases
        # 0 digits --> 1
        # 1 digit --> 1 if  digit != 0 else 0

        # Recursive Case

        # P(s, i) - # of ways to decode s[i:]

        # P(s, i) = 0 if s[i] == '0' else (
        #       P(s, i+1) + P(s, i+2) if int(s[i] + s[i+1]) <= 26 else P(s, i+1) )

        # Similar to Fibonacci Sequence only 2 previous terms required

        # Base Cases
        # 0 Digits
        n_2 = 1
        if not s:
            return n_2

        # 1 Digit
        n = len(s)
        n_1 = 1 if s[n - 1] != '0' else 0
        if n == 1:
            return n_1

        # Recursive Case
        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                res = 0
            else:
                if int(s[i:i + 2]) <= 26:
                    res = n_1 + n_2
                else:
                    res = n_1
            n_1, n_2 = res, n_1

        return res
