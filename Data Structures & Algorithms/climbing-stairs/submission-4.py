class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        array = [0] * n
        array[n-1] = 1
        array[n-2] = 2

        for i in range(n-3, -1, -1):
            array[i] = array[i+1] + array[i+2]
        
        return array[0]