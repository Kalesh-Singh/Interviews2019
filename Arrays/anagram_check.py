import collections


def anagram(s1, s2):
    count = collections.Counter(s1)
    count.subtract(s2)

    return sum(count.values()) == 0


def test_anagram():
    assert anagram('dog', 'god')


def test_not_anagram():
    assert not anagram('boy', 'girl')
