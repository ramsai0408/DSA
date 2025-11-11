class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        
        # First pass: identify which rows and columns have zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        # Second pass: set zeros
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0
        
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0


