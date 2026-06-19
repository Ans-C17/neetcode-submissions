class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        currPartition = []

        def dfs(i):
            if i >= len(s):
                res.append(currPartition.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    currPartition.append(s[i:j + 1])
                    dfs(j + 1)
                    currPartition.pop()
        
        dfs(0)
        return res
    
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False

            i, j = i + 1, j - 1
        
        return True