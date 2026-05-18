class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        dist = 0
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row, col) in visited or row < 0 or col < 0 or row == rows or col == cols or grid[row][col] == -1:
                        continue

                    visited.add((row, col))
                    q.append([row, col])

            dist += 1