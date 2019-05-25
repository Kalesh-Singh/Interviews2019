def find_max(arr):
    """Returns the  maximum element."""
    if len(arr) == 0:
        return None

    max_element = arr[0]

    for i in range(1, len(arr)):
        max_element = max(max_element, arr[i])

    return max_element


def test_max():
    arr = [34, 345123, 2, 1, 324, 765, 7, 6, 1]
    max_element = 345123
    assert find_max(arr) == max_element
