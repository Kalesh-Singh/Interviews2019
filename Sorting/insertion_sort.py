def insertion_sort(arr):
    size = len(arr)
    if size < 2:
        return arr
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def test_insertion_sort():
    sorted_arr = [2, 4, 4, 5, 13, 345, 451, 561]
    assert insertion_sort([345, 4, 4,  5, 2, 561, 451, 13]) == sorted_arr



