class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> int:
        # Solution 1 - Dynamic Programming
        # Start with the top and left edges

        rows = len(grid)
        cols = len(grid[0])

        res = [([None] * cols) for _ in range(rows)]

        res[0][0] = grid[0][0]

        for j in range(1, cols):
            res[0][j] = res[0][j - 1] + grid[0][j]

        for i in range(1, rows):
            res[i][0] = res[i - 1][0] + grid[i][0]

        for row in range(1, rows):
            for col in range(1, cols):
                res[row][col] = min(res[row - 1][col], res[row][col - 1]) + grid[row][col]

        return res[rows - 1][cols - 1]
