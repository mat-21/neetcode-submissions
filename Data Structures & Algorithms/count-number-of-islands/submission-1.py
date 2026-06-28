class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, seen = 0, set()

        rows, cols = len(grid), len(grid[0])

        def backtrack(row, col, idx):
            print(row, col, idx)
            if row >= rows or row < 0 or \
                    col >= cols or col < 0 or \
                    (row, col) in seen or \
                    grid[row][col] != '1':
                return

            seen.add((row, col))
            backtrack(row + 1, col, idx)
            backtrack(row - 1, col, idx)
            backtrack(row, col + 1, idx)
            backtrack(row, col - 1, idx)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    print('checking out', row, col)
                    backtrack(row, col, n + 1)
                    n += 1

        return n
