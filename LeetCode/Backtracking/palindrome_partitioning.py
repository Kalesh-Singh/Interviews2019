def isSolution(start, s):
    return start == len(s)


def isCandidate(s, start, end):
    # Is partition a palindrome ?
    # partition = s[start:end]
    # return partition == partition[::-1]
    i, j = start, end - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def search(solutions, state, s, start=0):
    # Have we reached a solution
    if isSolution(start, s):
        solutions.append(state.copy())
        return

    # Have we reached an impossibility --> Abort ?

    # Recurse with new candidates and state
    for end in range(start + 1, len(s) + 1):
        if isCandidate(s, start, end):
            # Update state
            state.append(s[start:end])

            search(solutions, state, s, end)

            # Restore state
            state.pop()


def solve(s):
    solutions = []
    search(solutions, [], s)
    return solutions


class Solution:
    def partition(self, s: str) -> 'List[List[str]]':
        return solve(s)
