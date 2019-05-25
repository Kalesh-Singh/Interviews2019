def _radix_counting_sort(arr, base, digit):
    """ Elements range from 0 to base-1."""
    counts = [[] for _ in range(base)]  # [0 .. base-1] = base # of elements
    for x in arr:
        # digit starts at [0 ... digits-1]
        d = (x // (base ** digit)) % base
        (counts[d]).append(x)
    return [item for sublist in counts for item in sublist]


def radix_sort(arr, d):
    # [0 ... (d-1)]
    for i in range(d):
        arr = _radix_counting_sort(arr, 10, i)
    return arr


def test_radix_sort():
    arr = [5432, 58, 221, 3429, 6843]
    sorted_arr = [58, 221, 3429, 5432, 6843]
    assert radix_sort(arr, 4) == sorted_arr
