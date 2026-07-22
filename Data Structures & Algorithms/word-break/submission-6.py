class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i == len(s):
                return True
            
            if i in dp:
                return dp[i]

            for j in range(len(wordDict)):
                length = len(wordDict[j])
                if s[i : i + length] == wordDict[j]:
                    res = dfs(i + length)
                    if res:
                        dp[i] = res
                        return True
            
            dp[i] = False
            return False
            
        return dfs(0)