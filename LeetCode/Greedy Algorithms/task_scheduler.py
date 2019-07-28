from collections import Counter
from heapq import heapify, heappush, heappop


class Solution:
    def leastInterval(self, tasks: 'List[str]', n: int) -> int:
        # Solution 1 - Sorting
        #         counts = Counter(tasks)
        #         counts = sorted(counts.values(), reverse=True)

        #         time = 0

        #         while counts[0] > 0:
        #             for i in range(n+1):
        #                 # Restart cool down time, since there is no more of that task
        #                 if counts[0] == 0:
        #                     break
        #                 if i < len(counts) and counts[i] > 0:
        #                     counts[i] -= 1
        #                 time += 1
        #             counts.sort(reverse=True)
        #         return time

        # Solution 2 - Max Heap
        #         counts = [-x for x in Counter(tasks).values()]
        #         heapify(counts)

        #         time = 0
        #         while counts:
        #             temp = []
        #             for i in range(n+1):
        #                 if counts:
        #                     if counts[0] < -1:
        #                         temp.append(heappop(counts)+1)
        #                     else:
        #                         heappop(counts)
        #                 time += 1
        #                 if not counts and not temp:
        #                     break
        #             for count in temp:
        #                 heappush(counts, count)
        #         return time

        # Solution 3 - Calculating the idle slots
        counts = sorted(Counter(tasks).values(), reverse=True)

        max_val = counts[0] - 1
        idle_slots = max_val * n

        for i in range(1, len(counts)):
            idle_slots -= min(counts[i], max_val)

        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
