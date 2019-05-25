from random import randint


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


def rand_partition(arr, p, r):
    # Make a random element the pivot before partitioning
    # to avoid the degenerate case.
    i = randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)


def randomized_select(arr, i, p=0, r=None):
    """Returns the ith element of the array in expected O(n) time."""
    if r is None:
        r = len(arr) - 1

    if i < 1 or i > r - p + 1:
        raise ValueError

    if p == r:
        return arr[p]

    q = rand_partition(arr, p, r)

    k = q - p + 1  # The kth element (We know what it is)

    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, i, p, q - 1)
    else:
        return randomized_select(arr, i - k, q + 1, r)


def test_randomized_select():
    arr = [34, 345123, 2, 1, 324, 765, 7, 6, 1]
    assert randomized_select(arr, 1) == 1
    assert randomized_select(arr, 2) == 1
    assert randomized_select(arr, 3) == 2
    assert randomized_select(arr, 4) == 6
    assert randomized_select(arr, 5) == 7
    assert randomized_select(arr, 6) == 34
    assert randomized_select(arr, 7) == 324
    assert randomized_select(arr, 8) == 765
    assert randomized_select(arr, 9) == 345123
