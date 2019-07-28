class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # Solution 1
        # When you encounter a digit that is less than the previous
        # decrease previous by 1 and make the rest 9
        # Repeat until no digit is encountered that is less than the previous

        #         digits = [int(x) for x in str(N)]
        #         n = len(digits)
        #         found = True
        #         while found:
        #             found = False
        #             for i in range(n - 1):
        #                 if digits[i] > digits[i+1]:
        #                     digits[i] -= 1
        #                     digits = digits[:i+1] + [9] * (n-1 - i);
        #                     found = True
        #                     break

        #         return int(''.join([str(x) for x in digits]))

        # Solution 2
        # Same idea as solution 1, except we iterate in reverse
        # so we don't have to repeat

        #         digits = [int(x) for x in str(N)]
        #         n = len(digits)

        #         marker = None
        #         for i in range(n-1, 0, -1):
        #             if digits[i] < digits[i-1]:
        #                 digits[i-1] -= 1
        #                 marker = i

        #         if marker is not None:
        #             digits = digits[:marker] + [9] * (n-marker)

        #         return int(''.join(map(str, digits)))

        # Solution 3 - Greedy
        # Build up the answer incrementally from the left
        # For each digit, find the smallest possible digit d,
        # such that answer + (d repeating) > N; that means
        # answer + (d-1 repeating) <= N. So we add d-1 to the
        # answer.

        digits = []
        A = list(map(int, str(N)))

        for i in range(len(A)):
            for d in range(1, 10):
                if digits + [d] * (len(A) - i) > A:
                    digits.append(d - 1)
                    break
            else:
                digits.append(9)
                # digits += [9] * (len(A) - i)
                # break

        return int(''.join(map(str, digits)))
