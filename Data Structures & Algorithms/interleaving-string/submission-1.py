class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # TC = 2^(m + n) because s3 = len(s1) + len(s2) = m + n
        # so s3 has two choices for m + n chars
        # we cross check which char from s1 or s2 to move when we take it from s3
        # that means two choices (s1 or s2 to choose) per char in s3

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]