def merge(arr, arr1, arr2):
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        merge_sort(arr1)
        merge_sort(arr2)
        merge(arr, arr1, arr2)
    return arr


def test_merge_sort():
    sorted_arr = [2, 4, 4, 5, 13, 345, 451, 561]
    assert merge_sort([345, 4, 4, 5, 2, 561, 451, 13]) == sorted_arr
