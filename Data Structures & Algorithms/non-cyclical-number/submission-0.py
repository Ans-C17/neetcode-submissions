class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        newNum = 0

        while n not in seen:
            if n == 0:
                if newNum == 1:
                    return True
                seen.add(newNum)
                n = newNum
                newNum = 0
            
            rem = n % 10
            sq = rem * rem
            n = n // 10
            newNum += sq

        return False