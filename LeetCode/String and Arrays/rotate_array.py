class Solution:
    def rotate(self, nums: 'List[int]', k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # SOLUTION 1 - Bubble Rotate
        # O(kn) Time O(1)Space
        # for _ in range(k):
        #     nums.insert(0, nums.pop())

        # SOLUTION 2 - Intermediate Array
        # O(n) Time O(n) Space
        # l = len(nums)
        # k = k % l
        # res = nums[:]

        # for i in range(l):
        #     nums[(k+i) % l] = res[i]

        # SOLUTION 3 - Reversal
        # O(n) Time O(1) Space
        # First divide the array in 2 parts
        # Then reverse the 2 parts
        # Reverse the entire array

        # [7,1,2,3,4,5,6] k= 3
        # [7,1,2,3] [4,5,6]
        # [3,2,1,7] [6,5,4]
        # [3,2,1,7,6,5,4]
        # [4,5,6,7,1,2,3]

        n = len(nums)

        if k > n:
            k = k % n

        i = i1 = 0
        i2 = n - k
        j1 = i2 - 1
        j = j2 = n - 1

        # Reverse first part
        while i1 < j1:
            nums[i1], nums[j1] = nums[j1], nums[i1]
            i1 += 1
            j1 -= 1

        # Reverse second part
        while i2 < j2:
            nums[i2], nums[j2] = nums[j2], nums[i2]
            i2 += 1
            j2 -= 1

        # Reverse entire array
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
