import pytest


def pair_sum(arr, sum):
    if len(arr) < 2:
        raise ValueError('Array must have 2 or more items')

    seen = set()
    pairs = []

    for num in arr:
        target = sum - num

        if target in seen:
            pairs.append((min(num, target), max(num, target)))
        else:
            seen.add(num)

    return len(pairs)


def test_value_error():
    with pytest.raises(ValueError):
        pair_sum([1], 4)


def test_two_pairs():
    assert pair_sum([1, 3, 2, 2], 4) == 2
