from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:
        # SOLUTION 1 - Using BFS
        word_dict = set(wordList)
        alphabet = list('abcdefghijklmnopqrstuvwxyz')

        def bfs(start, end):
            if end not in word_dict:
                return 0

            word = str(start)
            queue, visited = deque(), set()
            queue.append((word, 1))
            visited.add(word)

            while queue:
                word, count = queue.popleft()
                word = [letter for letter in word]  # List of chars is faster than splicing

                for i in range(len(word)):
                    original_char = word[i]
                    for letter in alphabet:
                        if word[i] != letter:
                            word[i] = letter
                            new_word = ''.join(word)
                            if new_word in word_dict and new_word not in visited:
                                if new_word == end:
                                    return count + 1
                                else:
                                    queue.append((new_word, count + 1))
                                    visited.add(new_word)
                    word[i] = original_char

            return 0

        return bfs(beginWord, endWord)
