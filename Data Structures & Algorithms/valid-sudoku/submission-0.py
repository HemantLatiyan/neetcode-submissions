class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowset = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rowset:
                    return False
                rowset.add(board[i][j])
            colset = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in colset:
                    return False
                colset.add(board[j][i])
        
        for square in range(9):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (square//3)*3 + r
                    col = (square%3)*3 + c
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

