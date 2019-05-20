from max_heap import MaxHeap


class MaxPriorityQueue(object):
    def __init__(self, arr=[]):
        self.max_heap = MaxHeap(arr)

    def __len__(self):
        return len(self.max_heap)

    def __getitem__(self, key):
        return self.max_heap[key]

    def __setitem__(self, key, value):
        self.max_heap[key] = value

    def __contains__(self, item):
        return item in self.max_heap

    def __str__(self):
        return str(self.max_heap)

    def __eq__(self, other):
        return self.max_heap == other

    def __iter__(self):
        for x in self.max_heap.arr:
            yield x

    def _pop(self):
        self.max_heap.arr.pop()
        self.max_heap.size -= 1

    def insert(self, item):
        pass

    def _parent(self, i):
        return self.max_heap.parent(i)

    def max(self):
        return self.max_heap[0]

    def extract_max(self):
        if len(self) < 1:
            raise IndexError("Heap Underflow")
        max_item = self[0]
        self[0] = self[len(self) - 1]
        self._pop()
        self.max_heap.max_heapify_rec(0)
        return max_item

    def increase_key(self, i, key):
        if key < self[i]:
            raise ValueError("New key is smaller than current key")

        # # Similar to shifting in insertion sort
        # self[i] = key
        # parent = self._parent(i)
        # while i > 0 and self[parent] < self[i]:
        #     self[i], self[parent] = self[parent], self[i]       # Costs 3 assignments
        #     i = parent
        #     parent = self._parent(i)

        # A more efficient approach using insertion sort technique
        parent = self._parent(i)
        while i > 0 and self[parent] < key:
            self[i] = self[parent]                              # Costs only 1 assignment
            i = parent
            parent = self._parent(i)
        self[i] = key

    def insert_key(self, key):
        self.max_heap.arr.append(float("-inf"))
        self.max_heap.size += 1
        self.increase_key(len(self) - 1, key)


def test_max():
    arr = [4, 1, 3, 3, 46, 2, 7, 2, 1, 9]
    max_pq = MaxPriorityQueue(arr)
    assert max_pq[0] == max(arr)


def test_extract_max():
    arr = [4, 1, 3, 3, 46, 2, 7, 2, 1, 9]
    max_arr = max(arr)
    max_pq = MaxPriorityQueue(arr)
    max_item = max_pq.extract_max()
    assert max_item == max_arr
    assert max_item not in max_pq


def test_increase_key():
    arr = [4, 1, 3, 3, 46, 2, 7, 2, 1, 9]
    max_pq = MaxPriorityQueue(arr)
    max_pq.increase_key(6, 50)
    max_item = max_pq[0]
    assert max_item == 50


def test_insert_key():
    arr = [4, 1, 3, 3, 46, 2, 7, 2, 1, 9]
    max_pq = MaxPriorityQueue(arr)
    old_len = len(max_pq)
    max_pq.insert_key(50)
    new_len = len(max_pq)
    assert new_len == old_len + 1
    max_item = max_pq[0]
    assert max_item == 50
