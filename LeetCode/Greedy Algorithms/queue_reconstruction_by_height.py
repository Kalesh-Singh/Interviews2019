class Solution:
    def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
        # Sort by height in descending order and then by k in ascending order
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        # Insert into output at the corresponding index
        for p in people:
            output.insert(p[1], p)
        return output
