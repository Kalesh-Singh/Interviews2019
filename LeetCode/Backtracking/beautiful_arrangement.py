#!/bin/python3

import math
import os
import random
import re
import sys


# We can use backtracking to solve this problem
def getCandidates(i, nums):
    return [(nums[j], nums[:j] + nums[j + 1:]) for j in range(len(nums)) if (nums[j] % i == 0) or (i % nums[j] == 0)]


def search(count, state, nums):
    # Have we found a solution
    if not nums:
        count[0] += 1
        return

    # Have we reached am impossibility?

    # Recurse with new candidates and state
    for c, otherNums in getCandidates(len(state) + 1, nums):
        print(otherNums)
        # Update state
        state.append(c)

        search(count, state, otherNums)

        # Restore state
        state.pop()


def solve(N):
    if N < 1:
        return 0
    count = [0]
    nums = [x for x in range(1, N + 1)]
    print(nums)
    search(count, [], nums)
    return count[0]


# Complete the countArrangement function below.
def countArrangement(N):
    return solve(N)
