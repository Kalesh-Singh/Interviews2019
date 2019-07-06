def valid(board: 'List[List[int]]', coords: 'tuple(x, y)') -> bool:
    rows = len(board)
    cols = len(board[0])
    x, y = coords
    return 0 <= x < rows and 0 <= y < cols


def find_word(board: 'List[List[int]]', word: str, i: int, coords: 'tuple(x, y)', seen: set) -> bool:
    if not valid(board, coords):
        return False

    if coords in seen:
        return False
    else:
        seen.add(coords)

    x, y = coords
    if word[i] != board[x][y]:
        return False

    i += 1

    if i == len(word):
        return True

    if find_word(board, word, i, (x - 1, y), set(seen)):
        return True
    if find_word(board, word, i, (x + 1, y), set(seen)):
        return True
    if find_word(board, word, i, (x, y - 1), set(seen)):
        return True
    if find_word(board, word, i, (x, y + 1), set(seen)):
        return True

    return False


class Solution:
    def exist(self, board: 'List[List[str]]', word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        for x in range(rows):
            for y in range(cols):
                if find_word(board, word, 0, (x, y), set()):
                    return True
        return False
