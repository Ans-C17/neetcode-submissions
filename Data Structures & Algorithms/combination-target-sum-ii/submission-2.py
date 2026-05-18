class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() #otherwise, [1,2] and [2,1] would be taken, we dont need duplicates, so sorting makes it [1,2] and [1,2]
        result = []

        def dfs(i, curr_list, total):
            if total == target:
                result.append(curr_list.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            curr_list.append(candidates[i])
            dfs(i+1, curr_list, total + candidates[i])

            curr_list.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                # 1. check if it overflows, we can have [1,1,1,1] and it can go out of bounds
                # 2. skip all duplicates as we are past the "choose" step, we dont wanna choose the same starting point as before 
                i += 1 
            dfs(i+1, curr_list, total)
        
        dfs(0, [], 0)
        return result

