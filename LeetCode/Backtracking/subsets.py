# We can use backtracking to find the subsets
def search(solutions, state, nums, k):
    # Have we reached a solution?
    if len(state) == k:
        solutions.append(state.copy())
        return

    # Have we reached an impossibility? --> Abort

    # Recurse with new state and candidates
    for c in getCandidates(state, nums):
        # Update the state
        state.append(c)

        search(solutions, state, nums, k)

        # Restore the state
        state.pop()


def getCandidates(state, nums):
    # Assume nums is sorted
    if not state:
        return nums
    return nums[nums.index(state[-1]) + 1:]


def solve(nums):
    solutions = [[], nums]
    for k in range(1, len(nums)):
        search(solutions, [], nums, k)
    return solutions


class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        return solve(nums)
