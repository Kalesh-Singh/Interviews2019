class Solution:
    def letterCasePermutation(self, S: str) -> 'List[str]':
        # "a"
        # [
        #   "a",
        #   "A"
        # ]
        #
        # "a1"
        # [
        #   "a1",
        #   "A1"
        # ]
        #
        # "a1b"
        # [
        #   "a1b",
        #   "a1B",
        #   "A1b",
        #   "A1B"
        # ]
        #
        # "a1b2"
        # [
        #   "a1b2",
        #   "a1B2",
        #   "A1b2",
        #   "A1B2"
        # ]

        # We can use a backtracking approach
        solutions = []
        self.search(solutions, '', S)
        return solutions

    def getCandidates(self, letter):
        if (letter.isdigit()):
            return [letter]
        else:
            return [letter, letter.swapcase()]

    def search(self, solutions, state, letters):
        # Have we found a solution ?
        if len(state) == len(letters):
            solutions.append(state)
            return

        # Have we reached an impossibility? --> Abort
        # Doesn't apply here

        # Recurse with new state and candidates.
        for letter in self.getCandidates(letters[len(state)]):
            # Update state
            state += letter

            self.search(solutions, state, letters)

            # Restore state
            state = state[:-1]
