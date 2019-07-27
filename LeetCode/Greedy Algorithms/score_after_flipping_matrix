class Solution:
        # 0 0 1 1
        # 1 0 1 0
        # 1 1 0 0
        
        # Toggle rows to make first col all 1s
        # 1 1 0 0
        # 1 0 1 0
        # 1 1 0 1
        
        # For every col other than the first
        # Toggle if # of 1s < # 0s
        # 1 1 1 1
        # 1 0 0 1
        # 1 1 1 0
    
    def toggleRow(self, A, row):
        cols = len(A[0])
        for i in range(cols):
            val = A[row][i]
            A[row][i] = 1 - val
    
    def toggleCol(self, A, col):
        rows = len(A)
        for i in range(rows):
            val = A[i][col]
            A[i][col] = 1 - val
    
    def getCountOfZeroesInCol(self, A, col):
        count = 0
        rows = len(A)
        for i in range(rows):
            if A[i][col] == 0:
                count += 1
        return count
    
    def getNum(self, A, row):
        strBinNum = ''.join(str(x) for x in A[row])
        return int(strBinNum, 2)
        
    def matrixScore(self, A: List[List[int]]) -> int:
        rows = len(A)
        cols = len(A[0])
        
        col = 0     # First row
        for row in range(rows):
            cell = A[row][col]
            if cell == 0:
                self.toggleRow(A, row)
        
        for col in range(1, cols):
            cellsPerCol = rows
            if self.getCountOfZeroesInCol(A, col) > cellsPerCol // 2:
                self.toggleCol(A, col)
        
        s = 0
        for row in range(rows):
            s += self.getNum(A, row)
            
        return s
