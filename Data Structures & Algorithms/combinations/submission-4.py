class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(curr, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return
            
            if curr == n+1:
                return
            
            arr.append(curr)
            dfs(curr+1, arr)
            arr.pop()
            dfs(curr+1, arr)
        
        dfs(1,[])

        return res