class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = float('-inf'), 0

        for num in nums:
            if currSum < 0: # negative sums dont help us, altho they are max contenders
                currSum = 0 # negative sums just make adding positive stuff give dimnishing returns so just reset
            
            currSum += num
            maxSum = max(maxSum, currSum) 
        
        return maxSum