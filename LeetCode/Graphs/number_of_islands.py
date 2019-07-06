def valid(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= x < rows and 0 <= y < cols


def flood_fill(grid, x, y):
    if not valid(grid, x, y):
        return
    if grid[x][y] != '1':
        return

    grid[x][y] = '0'

    flood_fill(grid, x - 1, y)
    flood_fill(grid, x + 1, y)
    flood_fill(grid, x, y - 1)
    flood_fill(grid, x, y + 1)


class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        # Solution 1 - Using Recursive flood fill algorithm
        count = 0

        if not grid:
            return count

        rows = len(grid)
        cols = len(grid[0])

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':  # Land
                    count += 1
                    # Replace all connecting land with water
                    flood_fill(grid, x, y)

        return count
