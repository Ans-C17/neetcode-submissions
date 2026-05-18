class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * (len(nums)+1) , [1] * (len(nums)+2)
        result = [1] * len(nums)

        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums), 0, -1):
            suffix[i] = suffix[i+1] * nums[i-1]
        
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i+2]
        
        return result