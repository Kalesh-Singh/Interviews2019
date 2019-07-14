# Question: Given a string s , find the length of the longest substring t that
# contains at most 2 distinct characters.

# Example 1:

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.

# Example 2:

# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.


def longest_substring(s):
    # Solution 1 - 2 Pointer Approach
    # Time O(n) Space O(1)
    max_substr = 0

    if not s:
        return max_substr

    n = len(s)

    unique_chars = {}

    start = 0
    for end in range(n):
        if s[end] not in unique_chars and len(unique_chars) == 2:
            # Get first unique element
            min_char = min(unique_chars, key=unique_chars.get)
            # Update start
            start = unique_chars[min_char] + 1
            # Remove the first unique element
            unique_chars.pop(min_char)
            # Put new char in the unique_chars (record the index it was last seen)
        unique_chars[s[end]] = end
        # Update max substr len
        curr_len = end - start + 1
        max_substr = max(max_substr, curr_len)
    return max_substr


def test_longest_substring():
    assert longest_substring('eceba') == 3
    assert longest_substring('ccaabbb') == 5
