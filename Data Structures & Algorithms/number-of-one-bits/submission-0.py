class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        while n:
            n &= (n-1)
            i += 1
        
        return i