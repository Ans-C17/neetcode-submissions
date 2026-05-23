class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # extract last bit
            res += (bit << (31 - i)) # now bit is last digit (say 00..001).. we left shift -> 1000000...00 (31 zeros)
        return res