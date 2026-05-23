class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            val = 0
            while i:
                i &= i-1
                val += 1
            res.append(val)
        
        return res