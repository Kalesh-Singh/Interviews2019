def find_min(arr):
    """Returns the  minimum element."""
    if len(arr) == 0:
        return None

    min_element = arr[0]

    for i in range(1, len(arr)):
        min_element = min(min_element, arr[i])

    return min_element


def test_min():
    arr = [34, 345123, 2, 1, 324, 765, 7, 6, 1]
    min_element = 1
    assert find_min(arr) == min_element
