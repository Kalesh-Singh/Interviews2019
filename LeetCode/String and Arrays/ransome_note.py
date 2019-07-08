from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_count = Counter(ransomNote)
        mag_count = Counter(magazine)

        mag_count.subtract(note_count)

        for letter in mag_count:
            if mag_count[letter] < 0:
                return False
        return True
