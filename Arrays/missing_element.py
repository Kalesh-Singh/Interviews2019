import collections


def missing_element(arr1, arr2):
    counter = collections.Counter(arr1)
    counter.subtract(arr2)
    return [x for x, count in counter.items() if count == 1][0]


def test_missing_5():
    assert missing_element([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]) == 5


# Linear Time and Constant Space using XOR
def missing_element_xor(arr1, arr2):
    result = 0

    for num in arr1 + arr2:
        result ^= num

    return result


def test_missing_5_xor():
    assert missing_element_xor([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]) == 5
