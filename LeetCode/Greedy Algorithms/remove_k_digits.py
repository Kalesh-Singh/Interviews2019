class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Solution 1 - Greedy Approach
        # Have a stack that we push each digit on.
        # Also have a variable ‘k’ that keeps track of how many characters we can remove.
        # While the previous character in our stack is larger than the current number,
        # and the length of the stack plus the remaining characters is greater than the
        # length of the number -k, we can remove it to get a smaller number.
        # We only add characters to the stack if the length of the stack is less than the
        # length of the number - k

        n = len(num)

        if k == n:
            return '0'

        stack = []
        for i in range(n):
            curr = int(num[i])

            while len(stack) > 0 and curr < stack[-1] and len(stack) + n - i > n - k:
                stack.pop()
            if len(stack) < n - k:
                stack.append(curr)

        return str(int(''.join([str(x) for x in stack])))
