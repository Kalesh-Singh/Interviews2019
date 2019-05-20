class MaxHeap(object):
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        self._build_max_heap()

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self.arr[key]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __str__(self):
        return str(self.arr)

    def __contains__(self, item):
        return item in self.arr

    # Another way to implement the iterator
    # def __iter__(self):
    #     self.i = 0
    #     return self
    #
    # def __next__(self):
    #     if self.i < len(self):
    #         ret = self[self.i]
    #         self.i += 1
    #         return ret
    #     else:
    #         raise StopIteration

    def __iter__(self):
        for x in self.arr:
            yield x

    def __eq__(self, other):
        return self.arr == other

    def _left(self, i):
        if i < 0 or i >= len(self):
            raise ValueError
        left = (2 * i) + 1
        if left >= len(self):
            return None
        return left

    def _right(self, i):
        if i < 0 or i >= len(self):
            raise ValueError
        right = (2 * i) + 2
        if right >= len(self):
            return None
        return right

    def parent(self, i):
        if i < 0 or i >= len(self):
            raise ValueError
        return i // 2

    def max_heapify_rec(self, i):
        """
        Assumes that the left and right sub trees of i are
        already valid min heaps
        """
        if i < 0 or i >= len(self):
            raise ValueError

        left = self._left(i)
        right = self._right(i)

        largest = i

        if left and self[left] > self[largest]:
            largest = left
        if right and self[right] > self[largest]:
            largest = right

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify_rec(largest)

    def max_heapify_iter(self, i):
        """Iterative max heapify implementation."""

        if i < 0 or i >= len(self):
            raise ValueError

        while True:
            left = self._left(i)
            right = self._right(i)

            largest = i

            if left and self[left] > self[largest]:
                largest = left
            if right and self[right] > self[largest]:
                largest = right

            if largest != i:
                self[i], self[largest] = self[largest], self[i]
                i = largest
            else:
                break

    def _build_max_heap(self):
        """For a zero indexed array implementation of a heap
        the leaves are the indices [floor(n/2) ... n-1]
        where n is the length of the array (the size of the heap)
        """
        # The subtrees at the leaves can be considered trivial min heaps
        # [(n//2)-1 ... 0]
        start = len(self) // 2 - 1
        for i in range(start, -1, -1):
            self.max_heapify_rec(i)


def test_build_max_heap():
    arr = [4, 1, 3, 3, 46, 2, 7, 2, 1, 9]
    heap = [46, 9, 7, 3, 4, 2, 3, 2, 1, 1]
    max_heap = MaxHeap(arr)
    assert max_heap == heap
