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

        # Appears recursive in nature
        # P(s) = P(s[1:]) + P(s[[2:]]) if int(s[:2]) <= 26 else P(s[1:])

        # Base Cases
        # 1 digit --> 1 if  digit != 0 else 0
        # 2 digits --> 1 if > 26 else 2

        # Similar to Fibonnaci Sequence only 2 previous terms required

        # TODO:
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

        n = len(s)

        if n == 1:
            n_2 = 0 if int(s[n - 1]) == 0 else 1  # n-2 term
            return n_2
        elif n == 2:
            n_2 = 0 if int(s[n - 1]) == 0 else 1  # n-2 term
            n_1 = n_2 + 1 if 0 < int(s[n - 2:]) <= 26 else n_2  # n-1 term
            return n_1

        n_2 = 0 if int(s[n - 1]) == 0 else 1  # n-2 term
        n_1 = n_2 + 1 if 0 < int(s[n - 2:]) <= 26 else n_2  # n-1 term

        for i in range(n - 3, -1, -1):
            if 0 < int(s[i:i + 2]) <= 26:
                res = n_1 + n_2
            else:
                res = n_1

            n_1, n_2 = res, n_1

        return res
