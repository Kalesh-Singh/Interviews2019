def four_sum(nums: 'List[int]', target: int) -> 'List[List[int]]':
    n = len(nums)
    nums.sort()
    result = set()
    for i in range(n):
        for j in range(i + 1, n):
            seen = {}
            for k in range(j + 1, n):
                comp = target - (nums[i] + nums[j] + nums[k])
                if comp in seen:
                    # result.add((nums[i], nums[j], nums[seen[comp]], nums[k]))
                    # This does not work for removing dups, i'm assuming it has to do with
                    # references and the values are not copied into the tuple?

                    # The below works :)
                    a = nums[i]
                    b = nums[j]
                    c = nums[seen[comp]]
                    d = nums[k]
                    result.add((a, b, c, d))
                else:
                    seen[nums[k]] = k
    return sorted([[num for num in res] for res in result])


print(four_sum([-3, -2, -1, 0, 0, 1, 2, 3], 0))

# Why is there a duplicate tuple in the result ? :/
# result is a SET of tuples. Is there some subtly i'm missing
# or is this a python bug ?


# Neater Solution
class Solution:
    def fourSum(self, nums: 'List[int]', target: int) -> 'List[List[int]]':
        n = len(nums)
        nums.sort()
        result = set()
        for i in range(n):
            for j in range(i+1, n):
                seen = set()
                for k in range(j+1, n):
                    a, b, d = nums[i], nums[j], nums[k]
                    c = target - (a + b + d)
                    if c in seen:
                        result.add((a, b, c, d))
                    else:
                        seen.add(d)
        return [[num for num in res] for res in result]