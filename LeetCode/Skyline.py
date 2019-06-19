from collections import namedtuple


class Point(namedtuple('Point', ['x', 'height', 'is_left'])):
    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            if self.is_left and other.is_left:
                # Look at building with higher height first
                return self.height > other.height
            if not self.is_left and not other.is_left:
                # Look at building with lower height first
                return self.height < other.height
            if self.is_left != other.is_left:
                # If end of one building is start of another
                # look at start point first
                return self.is_left
        else:
            return False


class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        n = len(buildings)
        points = []

        for b in buildings:
            points.append(Point(b[0], b[2], True))
            points.append(Point(b[1], b[2], False))

        # Sort the points
        # The comparator is used to deal with the edge cases
        points.sort()

        # Result list
        result = []

        # Max heap to keep track of max height
        max_heap = {0: 1}

        prev_max_height = 0

        for point in points:
            if point.is_left:
                if point.height in max_heap:
                    max_heap[point.height] += 1
                else:
                    max_heap[point.height] = 1
            else:
                if max_heap[point.height] == 1:
                    del max_heap[point.height]
                else:
                    max_heap[point.height] -= 1

            curr_max_height = max(max_heap.keys())

            if prev_max_height != curr_max_height:
                result.append([point.x, curr_max_height])
                prev_max_height = curr_max_height

        return result
