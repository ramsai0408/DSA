import collections

class Solution(object):
    def isValidSudoku(self, board):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grids = collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                # Check if number is in row, column, or grid
                if (num in rows[i] or
                    num in cols[j] or            # Use j for columns
                    num in grids[(i//3, j//3)]): # Use grids, not grid
                    return False
                rows[i].add(num)
                cols[j].add(num)
                grids[(i//3, j//3)].add(num)
        return True


        