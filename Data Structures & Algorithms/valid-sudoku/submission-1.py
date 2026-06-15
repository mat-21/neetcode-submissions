from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_box = defaultdict(list)
        columns = defaultdict(list)
        for row_idx, row in enumerate(board):
            row_vals = [val for val in row if val != '.']
            if len(row_vals) != len(set(row_vals)):
                return False

            for col_idx, cell in enumerate(row):
                sub_box_row_idx = str(row_idx // 3)
                sub_box_col_idx = str(col_idx // 3)
                sub_box_idx = sub_box_row_idx + sub_box_col_idx
                if cell != '.': 
                    if cell in sub_box[sub_box_idx]:
                        return False
                    sub_box[sub_box_idx].append(cell)

                    if cell in columns[col_idx]:
                        return False
                    columns[col_idx].append(cell)
        return True