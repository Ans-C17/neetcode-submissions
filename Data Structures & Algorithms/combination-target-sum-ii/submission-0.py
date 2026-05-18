class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(i, curr_list, total):
            if total == target:
                if curr_list not in result:
                    result.append(curr_list.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            curr_list.append(candidates[i])
            dfs(i+1, curr_list, total + candidates[i])

            curr_list.pop()
            dfs(i+1, curr_list, total)
        
        dfs(0, [], 0)
        return result

