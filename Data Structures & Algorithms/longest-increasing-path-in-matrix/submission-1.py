class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {} # (r, c) -> maxLen

        def dfs(r, c, prevVal):
            if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] <= prevVal:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1 # min length would be one nig
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            
            dp[(r, c)] = res
            return res
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, -1)
        
        return max(dp.values())