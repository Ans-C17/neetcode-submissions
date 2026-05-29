class Solution:
    def checkValidString(self, s: str) -> bool:
        # leftMax assumes asterisks are a left bracket
        # leftMin positive assumes asterisks are a right bracket
        # leftMin resetted assumes asterisk is an empty space instead 

        leftMin = leftMax = 0
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            
            if leftMin == -1: leftMin = 0
            if leftMax == -1: return False
        
        return leftMin == 0