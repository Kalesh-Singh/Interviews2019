from heapq import heappush, heappop


class Solution:
    def scheduleCourse(self, courses: 'List[List[int]]') -> int:
        # Solution 1 - Using Max Heap and Sorting
        # Sort based on close date and then duration
        courses.sort(key=lambda x: (x[1], x[0]))
        print(courses)

        # Keep max heap of courses taken based on duration
        max_heap = []

        time = 0

        for duration, close_date in courses:
            # Try to take the course
            if time + duration <= close_date:
                heappush(max_heap, -duration)                       # heappush(max_heap, duration)
                time += duration
            # If we can't take the course directly try
            # Replacing a course of longer duration
            # with this one
            elif len(max_heap) > 0 and max_heap[0] < (-duration):   # max_heap[0] > duration
                time += (duration + heappop(max_heap))              # time += duration - max_duration
                heappush(max_heap, -duration)                       # heappush(max_heap, duration)

        return len(max_heap)
