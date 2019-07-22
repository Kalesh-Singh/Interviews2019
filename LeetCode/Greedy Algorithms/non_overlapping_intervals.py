class Solution:
    def overlaps(self, int1: 'List[int]', int2: 'List[int]') -> bool:
        return int1[1] > int2[0]

    def eraseOverlapIntervals(self, intervals: 'List[List[int]]') -> int:
        # Solution 1 - Greedy Approach
        # Time O(nlogn), Space O(1)

        # Sort the intervals by end time
        intervals.sort(key=lambda x: x[1])

        remove_count = 0

        if not intervals or len(intervals) < 2:
            return remove_count

        last_valid_interval_idx = 0

        for i in range(1, len(intervals)):
            if self.overlaps(intervals[last_valid_interval_idx], intervals[i]):
                remove_count += 1
            else:
                last_valid_interval_idx = i

        return remove_count
