import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # col / 3 , row / 3

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":  # if sudoku [r][c] box empty than we skip it
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])  # val occured first time than we have to add to the map
                rows[r].add(board[r][c])  # val occured first time than we have to add to the map
                squares[(r // 3, c // 3)].add(board[r][c])  # val occured first time than we have to add to the map

        return True
