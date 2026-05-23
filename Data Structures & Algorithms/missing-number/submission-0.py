class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # realSum = (len(nums) * (len(nums) + 1))//2
        # return realSum - sum(nums)

        res = nums[0]
        for n in range(1, len(nums)):
            res ^= nums[n]

        for i in range(len(nums) + 1):
            res ^= i

        return res