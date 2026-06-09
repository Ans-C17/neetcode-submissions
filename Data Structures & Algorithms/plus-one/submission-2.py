class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for i in range(len(digits) - 1, -1, -1):
            tot = digits[i] + carry
            carry = tot // 10
            tot = tot % 10
            res.append(tot)
        
        if carry: res.append(carry)
        return res[::-1]