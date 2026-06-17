class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        maxVal = 0

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][j] == "1" and dp[i + 1][j + 1] and dp[i + 1][j] and dp[i][j + 1]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = int(matrix[i][j])
                
                maxVal = max(maxVal, dp[i][j])
        return maxVal**2