class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums2):
            if len(nums2) == 1:
                return nums2[0]
            
            dp = [0] * len(nums2)
            dp[0] = nums2[0]
            dp[1] = max(nums2[0], nums2[1])

            for i in range(2, len(nums2)):
                dp[i] = max(dp[i - 1], nums2[i] + dp[i - 2])

            return dp[-1]
        

        if len(nums) == 1:
            return nums[0]
        
        return max(helper(nums[1:]), helper(nums[:-1]))
