# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] find the minimum number of conference rooms required

from heapq import heappush, heappop


def min_meeting_rooms(intervals):
    # Greedy Approach
    # Sort the intervals by start time
    # Schedule the meeting with the earliest start time
    # Keep track of the earliest end time
    # If earliest end time > next start time
    # increment the counter

    intervals.sort(key=lambda x: x[0])

    rooms = 1

    # Keep a min heap of the earliest end times
    min_heap = [float('-inf')]

    for start, end in intervals:
        if min_heap[0] > start:
            rooms += 1
        else:
            heappop(min_heap)
        heappush(min_heap, end)
    return rooms


def test_min_meeting_rooms():
    intervals = [[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]]
    assert min_meeting_rooms(intervals) == 2
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert min_meeting_rooms(intervals) == 2
