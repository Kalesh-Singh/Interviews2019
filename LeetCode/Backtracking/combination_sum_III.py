# Explore all possible combinations
# and select the appropriate ones

# We can use a back tracking approach
# to achieve this.


def search(solutions, state, n, k):
    # Have we reached a solution?
    print(state)
    if isSolution(n, k):
        solutions.append(state.copy())
        return

    # if len(state) == k:
    #    return

    # Have we reached an impossibility?

    # If we cannot possibly meet the sum with the remaining nums
    # abort
    # if 9 * k < n:
    #     return

    # An improvement to the above
    max_rem = 1
    for i in range(10 - k, 10):
        max_rem *= i
    if max_rem < n:
        return

    # If the remaining sum is less than the smallest available
    # candidate, abort
    if len(state) > 0 and n <= state[-1]:
        return

    # Recurse with new states and candidates
    for candidate in getCandidates(state):
        # Update the state
        state.append(candidate)

        search(solutions, state, n - candidate, k - 1)

        # Restore the state
        state.pop()


def getCandidates(state):
    min_candidate = state[-1] + 1 if state else 1
    return [c for c in range(min_candidate, 10)]


def isSolution(n, k):
    return n == 0 and k == 0
    # return len(state) == k and sum(state) == n


def solve(n, k):
    solutions = []
    search(solutions, [], n, k)
    return solutions


class Solution:
    def combinationSum3(self, k: int, n: int) -> 'List[List[int]]':
        return solve(n, k)
