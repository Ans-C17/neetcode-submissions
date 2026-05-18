class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(curr, total, i):
            if total == target:
                result.append(curr.copy())
                return
            
            if i == len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            backtrack(curr, total + candidates[i], i+1)

            curr.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(curr, total, i+1)
        
        backtrack([], 0, 0)
        return result