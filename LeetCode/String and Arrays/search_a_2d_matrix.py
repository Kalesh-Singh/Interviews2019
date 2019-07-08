def getIndex(row, col, num_cols):
    return row * num_cols + col


def getRowCol(index, num_cols):
    return index // num_cols, index % num_cols


class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        end = getIndex(rows - 1, cols - 1, cols)

        while start <= end:
            mid = (start + end) // 2
            r, c = getRowCol(mid, cols)

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
