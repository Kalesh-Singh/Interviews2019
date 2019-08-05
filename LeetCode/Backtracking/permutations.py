class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        # []
        # []

        # [1]
        # [
        #   [1]
        # ]

        # [1, 2]
        # [
        #   [1, 2]
        #   [2, 1]
        # ]

        # [1, 2, 3]
        # [
        #   [1, 2, 3]
        #   [1, 3, 2]
        #   [2, 1, 3]
        #   [2, 3, 1]
        #   [3, 1, 2]
        #   [3, 2, 1]
        # ]

        # Appears we can solve by using backtracking

        # search - Will be our recursive function

        solutions = []
        self.search(solutions, [], nums)
        return solutions

    def search(self, solutions, state, candidates):
        # Have we reached a solution
        if not candidates:
            solutions.append(state.copy())
            return

        # Have we reached an impossibililty --> Abort
        # Does not apply in this problem

        # Recurse with new state and candidates
        for i, candidate in enumerate(candidates):
            # Update state
            state.append(candidate)

            # Make recursive call with new candidates
            self.search(solutions, state, candidates[:i] + candidates[i + 1:])

            # Restore state
            state.pop()
