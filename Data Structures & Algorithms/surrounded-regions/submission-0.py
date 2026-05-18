class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited, safe = set(), set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, visited):
            if (r, c) in visited or r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            
            visited.add((r, c))
            safe.add((r, c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited)
        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c, visited)

            if board[ROWS-1][c] == "O":
                dfs(ROWS-1, c, visited)
        
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0, visited)

            if board[r][COLS-1] == "O":
                dfs(r, COLS-1, visited)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"

