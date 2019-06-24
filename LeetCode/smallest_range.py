from collections import namedtuple
from heapq import heappush, heappop


class Point(namedtuple('Point', ['val', 'lst', 'next_idx'])):
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def smallestRange(self, nums: 'List[List[int]]') -> 'List[int]':
        # SOLUTION 1 - Min Heap of k elements
        # O(nlogk) Time - where n is the total number of elements
        # in all the lists and k is the number of lists.
        k = len(nums)
        min_heap = []
        max_heap = []

        # Initialize heaps
        for i in range(k):
            val = nums[i][0]
            heappush(min_heap, Point(val, i, 1))
            heappush(max_heap, -val)
        min_range = [min_heap[0].val, -max_heap[0]]
        min_range_val = min_range[1] - min_range[0]

        while min_heap:
            # Maintain min heap
            lp = heappop(min_heap)
            if lp.next_idx >= len(nums[lp.lst]):
                break
            val = nums[lp.lst][lp.next_idx]
            p = Point(val, lp.lst, lp.next_idx + 1)
            heappush(min_heap, p)

            # Maintain max heap
            while -max_heap[0] < lp.val:
                heappop(max_heap)
            heappush(max_heap, -val)

            # Update range
            curr_range = [min_heap[0].val, -max_heap[0]]
            curr_range_val = curr_range[1] - curr_range[0]
            if curr_range_val < min_range_val:
                min_range = curr_range
                min_range_val = curr_range_val

        return min_range
