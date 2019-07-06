def valid(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= x < rows and 0 <= y < cols


def flood_fill(grid, x, y):
    if not valid(grid, x, y):
        return
    if grid[x][y] != 'O':
        return

    grid[x][y] = '-'

    flood_fill(grid, x - 1, y)
    flood_fill(grid, x + 1, y)
    flood_fill(grid, x, y - 1)
    flood_fill(grid, x, y + 1)


class Solution:
    def solve(self, board: 'List[List[str]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        # First row
        for y in range(cols):
            flood_fill(board, 0, y)

        # Last row
        for y in range(cols):
            flood_fill(board, rows - 1, y)

        # First col
        for x in range(rows):
            flood_fill(board, x, 0)

        # Last col
        for x in range(rows):
            flood_fill(board, x, cols - 1)

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == '-':
                    board[x][y] = 'O'
