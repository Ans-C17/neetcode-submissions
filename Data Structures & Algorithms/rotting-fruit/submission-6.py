class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols =  len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if row < 0 or col < 0 or row == rows or col == cols or grid[row][col] == 2 or grid[row][col] == 0:
                        continue
                    if grid[row][col] == 1:
                        q.append((row, col))
                        grid[row][col] = 2
                        fresh -= 1
            
            time += 1

        return time if fresh == 0 else -1
