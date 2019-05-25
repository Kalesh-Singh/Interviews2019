def find_min_max(arr):
    """Returns the minimum and maximum elements (min, max)."""
    min_element = None
    max_element = None
    start = None

    if len(arr) == 0:
        return min_element, max_element

    # If even
    if len(arr) % 2 == 0:
        if arr[0] < arr[1]:
            min_element = arr[0]
            max_element = arr[1]
        else:
            min_element = arr[1]
            max_element = arr[0]
        start = 2
    else:
        min_element = arr[0]
        max_element = arr[0]
        start = 1

    """ 
    This technique uses 3 comparisons per pair of elements,
    as opposed to the more obvious 2 comparisons per 
    single element.
    """
    for i in range(start, len(arr)-1):
        x = arr[i]
        y = arr[i + 1]

        if x < y:
            p_min = x
            p_max = y
        else:
            p_min = y
            p_max = x

        if p_min < min_element:
            min_element = p_min
        if p_max > max_element:
            max_element = p_max

    return min_element, max_element


def test_min_max():
    arr = [34, 345123, 2, 1, 324, 765, 7, 6, 1]
    max_element = 345123
    min_element = 1
    assert find_min_max(arr) == (min_element, max_element)
