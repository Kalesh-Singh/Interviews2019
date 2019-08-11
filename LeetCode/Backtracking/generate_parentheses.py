# We can use backtracking to accomplish this


def getCandidates(n, open_count, close_count):
    if open_count == 0:
        return '('
    if open_count < n:
        if close_count < open_count:
            return '()'
        return '('
    if close_count < n:
        return ')'


def isSolution(state, n):
    return len(state) == 2 * n


def search(solutions, state, n, open_count=0, close_count=0):
    # Have re reached a solution
    if isSolution(state, n):
        solutions.append(''.join(state))
        return

    # Have we reached an impossibility? --> Abort
    # Not applicable in this case

    # Recurse with new candidates and state
    for c in getCandidates(n, open_count, close_count):
        # Update state
        state.append(c)

        search(solutions, state, n,
               open_count if c == ')' else open_count + 1,
               close_count if c == '(' else close_count + 1)

        # Restore state
        state.pop()


def solve(n):
    solutions = []
    search(solutions, [], n)
    return solutions


class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        return solve(n)
