class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)
        
        dp = [[0] * (cols + 1) for i in range(rows + 1)]
        dp[rows][cols] = 0

        for i in range(rows + 1):
            dp[i][cols] = rows - i
        
        for i in range(cols + 1):
            dp[rows][i] = cols - i

        print(dp)

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    minval = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
                    dp[i][j] = 1 + minval
        return dp[0][0]

