def partition(arr, p, r):
    x = arr[r]  # pivot
    i = p - 1  # All elements before index i are <= pivot
    # Exclude the last element (pivot) hence [p ... r-1]
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # a[i+1] is the first element greater than the pivot value
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quick_sort(arr, p=0, r=None):
    if r is None:
        r = len(arr) - 1
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)

    return arr


def test_quick_sort():
    sorted_arr = [2, 4, 4, 5, 13, 345, 451, 561]
    arr = [345, 4, 4, 5, 2, 561, 451, 13]
    assert quick_sort(arr) == sorted_arr
