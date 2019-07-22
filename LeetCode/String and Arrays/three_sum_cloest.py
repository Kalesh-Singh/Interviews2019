def cloest(nums: 'Sorted array', start_idx, end_idx, target):
    start, end = start_idx, end_idx
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return target
        elif nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
    if end < start_idx:
        return nums[start]
    if start > end_idx:
        return nums[end]
    return nums[end] if start > end else nums[start]


def twoSumClosest(nums: 'Sorted array', start_idx, end_idx, target):
    res = float('inf')
    for i in range(start_idx, end_idx):
        num = nums[i]
        c = cloest(nums, i + 1, end_idx, target - num)
        if abs((c + num) - target) < abs(res - target):
            res = c + num
    return res


def threeSumClosest(nums, target):
    nums = sorted(nums)
    res = float('inf')
    n = len(nums)
    for i in range(n - 2):
        num = nums[i]
        c = twoSumClosest(nums, i + 1, n - 1, target - num)
        if abs((c + num) - target) < abs(res - target):
            res = c + num
    return res
