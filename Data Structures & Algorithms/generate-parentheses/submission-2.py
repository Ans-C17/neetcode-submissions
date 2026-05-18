class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(leftCount, rightCount, curr):
            if leftCount == rightCount == n:
                result.append("".join(curr.copy()))
                return
                
            if leftCount < n:
                curr.append("(")
                backtrack(leftCount+1, rightCount, curr)
                curr.pop()

            if rightCount < leftCount:
                curr.append(")")
                backtrack(leftCount, rightCount+1, curr)
                curr.pop()
            

        backtrack(1, 0, ["("])
        return result