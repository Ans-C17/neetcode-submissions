class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        res = float("-inf")
        for i in range(len(nums)):
            currSum += nums[i]
            res = max(res, currSum)

            if currSum < 0:
                currSum = 0
        
        return res