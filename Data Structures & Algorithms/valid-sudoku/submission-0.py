from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # MT = my thoughts
        # Each row must contain the digits 1-9 without duplicates. - MT: I need a set to ensure uniqueness across rows and columns, Any numbers below 1 or greater than 9 are not valid, there are 9 3x3 sub-boxes in the grid and these must also contain 1-9 without duplications. So rows, columns, and each sub-box must be 1-9 int and there must not be any duplicates. Return false if any of these constraints are broken or true if all constraints pass. Based on the board it looks like a list of lists of the string type as the function signature tells me I can assume. It does not seem like I need

        rows = defaultdict(set) # {0: "1", "2", "3"}
        cols = defaultdict(set) # {0: "1", "4", "5", "7"}
        grids = defaultdict(set) # {0: "1", "2", "4", "9", "8"}


        for r in range(9):
            for c in range(9):
                grid = (r // 3, c // 3)
                value = board[r][c]
                if value == ".":
                    continue
                if value in rows[r] or value in cols[c] or value in grids[grid]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                grids[grid].add(value)
    
        return True

            







        