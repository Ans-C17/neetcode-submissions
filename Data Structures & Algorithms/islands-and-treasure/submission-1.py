class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row == rows or col == cols or (row, col) in visit or grid[row][col] == -1:
                        continue
                    
                    visit.add((row, col))
                    q.append([row, col])
            dist += 1