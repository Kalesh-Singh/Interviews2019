from max_heap import MaxHeap


def heap_sort(arr):
    max_heap = MaxHeap(arr)

    # from [len-1 ... 1]
    for i in range(len(max_heap) - 1, 0, -1):
        max_heap[0], max_heap[i] = max_heap[i], max_heap[0]
        max_heap.size -= 1
        max_heap.max_heapify_rec(0)

    return max_heap.arr

def test_heap_sort():
    sorted_arr = [2, 4, 4, 5, 13, 345, 451, 561]
    arr = [345, 4, 4, 5, 2, 561, 451, 13]
    assert heap_sort(arr) == sorted_arr

