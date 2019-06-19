class MinHeap(object):
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        self._build_min_heap()

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self.arr[key]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __str__(self):
        return str(self.arr)

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

    def _parent(self, i):
        if i < 0 or i >= len(self):
            raise ValueError
        return (i - 1) // 2

    def _min_heapify_rec(self, i):
        """
        Assumes that the left and right sub trees of i are
        already valid min heaps
        """
        if i < 0 or i >= len(self):
            raise ValueError

        left = self._left(i)
        right = self._right(i)

        smallest = i

        if left and self[left] < self[smallest]:
            smallest = left
        if right and self[right] < self[smallest]:
            smallest = right

        if smallest != i:
            self[i], self[smallest] = self[smallest], self[i]
            self._min_heapify_rec(smallest)

    def _min_heapify_iter(self, i):
        """Iterative min heapify implementation."""

        if i < 0 or i >= len(self):
            raise ValueError

        while True:
            left = self._left(i)
            right = self._right(i)

            smallest = i

            if left and self[left] < self[smallest]:
                smallest = left
            if right and self[right] < self[smallest]:
                smallest = right

            if smallest != i:
                self[i], self[smallest] = self[smallest], self[i]
                i = smallest
            else:
                break

    def _build_min_heap(self):
        """For a zero indexed array implementation of a heap
        the leaves are the indices [floor(n/2) ... n-1]
        where n is the length of the array (the size of the heap)
        """
        # The subtrees at the leaves can be considered trivial min heaps
        # [(n//2)-1 ... 0]
        start = len(self) // 2 - 1
        for i in range(start, -1, -1):
            self._min_heapify_rec(i)


def test_build_min_heap():
    arr = [4, 1, 3, 3, 46, 2, 7, 2, 1, 9]
    heap = [1, 1, 2, 2, 9, 3, 7, 4, 3, 46]
    min_heap = MinHeap(arr)
    assert min_heap == heap
