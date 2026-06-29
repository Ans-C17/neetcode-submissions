class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def isPali(i, j):
            nonlocal res
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
        
        for i in range(len(s)):
            isPali(i, i)
            isPali(i, i + 1)
        
        return res