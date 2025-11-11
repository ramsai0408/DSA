from collections import defaultdict

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        # Preload existing numbers into sets
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grid[(i//3, j//3)].add(board[i][j])

        def backtrack(i, j):

            if i == 9:
                return True  # Sudoku solved

            new_i = i + (j + 1) // 9
            new_j = (j + 1) % 9

            # Skip pre-filled cells
            if board[i][j] != '.':
                return backtrack(new_i, new_j)

            for num in "123456789":
                if num not in rows[i] and num not in cols[j] and num not in grid[(i//3, j//3)]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    grid[(i//3, j//3)].add(num)

                    if backtrack(new_i, new_j):
                        return True

                    # Undo (backtrack)
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    grid[(i//3, j//3)].remove(num)

            return False  # no valid number found

        backtrack(0, 0)


        


        