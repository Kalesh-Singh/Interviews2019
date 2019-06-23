class Solution:
    def evalRPN(self, tokens: 'List[str]') -> int:
        # SOLUTION 1 - Stack
        # O(n) Time O(n) Space

        operators = set('+-*/')

        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                if token == '+':
                    stack.append(x + y)
                elif token == '-':
                    stack.append(x - y)
                elif token == '*':
                    stack.append(x * y)
                else:
                    # Note: Be careful with the division
                    # 5 // 10 = 0
                    # 5 // -10 = - 1
                    stack.append(int(x / y))

        return stack[0]
