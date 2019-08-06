def search(solutions, state, candidates_start, candidates_end, k):
    # Have we reached a solution ?
    if len(state) == k:
        solutions.append(state.copy())
        return

    # Have we reached an impossibility ? --> Abort

    # Recurse with new state and candidates
    for num in range(candidates_start, candidates_end + 1):
        # Update state
        state.append(num)

        search(solutions, state, num + 1, candidates_end, k)

        # Restore state
        state.pop()


class Solution:
    def combine(self, n: int, k: int) -> 'List[List[int]]':
        # We can use backtracking

        solutions = []
        search(solutions, [], 1, n, k)
        return solutions
