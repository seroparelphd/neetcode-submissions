from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subboxes = defaultdict(set)
        # print(1//3)
        # print(4//3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                digit = board[r][c]
                if digit in rows[r] or digit in cols[c] or digit in subboxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                subboxes[(r // 3, c // 3)].add(digit)
        print(f"rows = {rows}")
        print(f"cols = {cols}")
        print(f"subboxes = {subboxes}")
        return True
            
