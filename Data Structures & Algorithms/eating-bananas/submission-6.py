class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            timeToFinish = 0
            m = (l + r) // 2

            for p in piles:
                timeToFinish += math.ceil(p / m)
            
            if  timeToFinish <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res