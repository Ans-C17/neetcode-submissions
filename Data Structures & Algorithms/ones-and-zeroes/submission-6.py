class Solution:
    def find01(self, s):
        zero, one = 0, 0
        for c in s:
            if c == "0": zero += 1
            else: one += 1
        
        return zero, one

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {} # dp[(i, m, n)] = max len of valid subset starting there
        def dfs(i, fake_m, fake_n):
            if i == len(strs):
                return 0
            
            if (i, fake_m, fake_n) in dp:
                return dp[(i, fake_m, fake_n)]
            
            zero, one = self.find01(strs[i])
            
            take = 0
            if fake_m >= zero and fake_n >= one:
                take = 1 + dfs(i + 1, fake_m - zero, fake_n - one)

            skip = dfs(i + 1, fake_m, fake_n)
            res = max(take, skip)
            dp[(i, fake_m, fake_n)] = res
            return res

        return dfs(0, m, n)
