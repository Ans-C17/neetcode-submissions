class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl =  set(), set()

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c, visited, prevHeight):
            if r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight or (r, c) in visited:
                return
            
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
            
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        
        return res