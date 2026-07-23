class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, curList):
            if i > n:
                if len(curList) == k:
                    res.append(curList.copy())
                return
            
            curList.append(i)
            backtrack(i + 1, curList)
            curList.pop()
            backtrack(i + 1, curList)
        
        backtrack(1, [])
        return res