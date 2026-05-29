class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-infinity")
        currSum = 0
        l = r = 0
        while r < len(nums):
            currSum += nums[r]
            res = max(res, currSum)
            r += 1

            if currSum < 0:
                currSum = 0
                l = r + 1
        
        return res