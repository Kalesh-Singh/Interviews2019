def counting_sort(arr, k):
    """ Elements range from 0 to k."""
    sorted_arr = [None] * len(arr)
    counts = [0] * (k + 1)  # [0 .. k] = k+1 elements
    for x in arr:
        counts[x] += 1
    # counts[i] now contains the number of elements == i
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    # counts[i] now contains the number of elements <= i
    for i in range(len(arr) - 1, -1, -1):
        elem = arr[i]
        sorted_arr[counts[elem]-1] = elem
        counts[elem] -= 1
    return sorted_arr


def test_counting_sort():
    sorted_arr = [2, 4, 4, 5, 12, 15, 20, 21]
    arr = [20, 4, 4, 5, 2, 21, 15, 12]
    assert counting_sort(arr, 21) == sorted_arr
